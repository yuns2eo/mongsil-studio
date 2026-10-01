#!/usr/bin/env python3
"""Natural-language CLI for creating and editing the official MONGSIL."""

from __future__ import annotations

import argparse
import base64
from contextlib import ExitStack
from datetime import datetime
import json
import os
from pathlib import Path
import re
import sys
from uuid import uuid4


ROOT = Path(__file__).resolve().parent
REFERENCES = ROOT / "references"
OUTPUT = ROOT / "output"
MODEL = "gpt-image-2.5-sunburst"
TURNAROUNDS = {
    "front": "MONGSIL_Front.png",
    "three_quarter": "MONGSIL_Left_3Q.png",
    "profile": "MONGSIL_Left_Profile.png",
    "back": "MONGSIL_Back.png",
}
DETAILS = {
    "paw": "MONGSIL_Paw_Inner.png",
    "sole": "MONGSIL_Foot_Sole.png",
    "tail": "MONGSIL_Tail.png",
}


def read_required(relative_path: str) -> str:
    path = ROOT / relative_path
    if not path.is_file():
        raise ValueError(f"필수 프로젝트 파일이 없습니다: {path}")
    return path.read_text(encoding="utf-8")


def official_image(filename: str) -> Path:
    path = REFERENCES / filename
    if not path.is_file():
        raise ValueError(f"공식 레퍼런스가 없습니다: {path}")
    return path


def view_for(request: str) -> str:
    lower = request.lower()
    if re.search(r"후면|뒷모습|뒤에서|등을 보|back view|rear view", lower):
        return "back"
    if re.search(r"측면|옆모습|옆에서|프로필|profile|side view", lower):
        return "profile"
    if re.search(r"3\s*[/／-]\s*4|3q|three.quarter|쿼터|사선", lower):
        return "three_quarter"
    if re.search(r"정면|앞모습|front view|frontal", lower):
        return "front"
    return "front"


def select_references(request: str, view: str) -> tuple[Path, Path | None, list[Path]]:
    primary = official_image(TURNAROUNDS[view])
    lower = request.lower()
    # Add one adjacent turnaround only when the requested turn or pose needs it.
    secondary = None
    if re.search(r"회전|돌아서|고개를 돌|비틀|뒤돌|반대쪽|turn(?:ing)?|rotate|twist", lower):
        adjacent = {
            "front": "three_quarter",
            "three_quarter": "front",
            "profile": "three_quarter",
            "back": "three_quarter",
        }[view]
        secondary = official_image(TURNAROUNDS[adjacent])

    details = []
    if re.search(r"손바닥|발바닥이 아닌 앞발 안쪽|paw pad|palm", lower):
        details.append(official_image(DETAILS["paw"]))
    if re.search(r"발바닥|발의 밑|foot sole|sole pad", lower):
        details.append(official_image(DETAILS["sole"]))
    if re.search(r"꼬리.*(?:크게|자세히|강조|클로즈업|복잡)|(?:tail).*(?:close.up|detail|prominent)", lower):
        details.append(official_image(DETAILS["tail"]))
    return primary, secondary, details


def first_match(request: str, patterns: list[str], default: str) -> str:
    for pattern in patterns:
        match = re.search(pattern, request, re.IGNORECASE)
        if match:
            return match.group(0).strip()
    return default


def interpret(request: str, view: str) -> dict[str, str]:
    """Extract explicit cues; keep the complete original request in the prompt."""
    return {
        "action_and_pose": request,
        "expression": first_match(
            request,
            [r"(?:웃|미소|기뻐|신나|놀라|졸려|걱정|울|화나|집중)[^\s,.!?]*", r"happy|smil\w*|surpris\w*|sleepy|worried|crying|angry|focused"],
            "요청한 행동에 자연스럽게 맞는 기본 표정",
        ),
        "view": {
            "front": "front view",
            "three_quarter": "weak or normal 3/4 view",
            "profile": "profile view",
            "back": "back view",
        }[view],
        "outfit": first_match(
            request,
            [r"[^\s,.!?]*(?:셰프복|유니폼|드레스|재킷|코트|티셔츠|바지|모자|옷)[^\s,.!?]*", r"[^\s,.!?]*(?:outfit|uniform|dress|jacket|coat|shirt|pants|hat)[^\s,.!?]*"],
            "none unless explicitly requested in the original request",
        ),
        "props": first_match(
            request,
            [r"[^\s,.!?]*(?:사과|스마트폰|휴대폰|전화기|책|상자|숟가락|컵|우산|꽃|가방|도구)[^\s,.!?]*", r"[^\s,.!?]*(?:apple|phone|book|box|spoon|cup|umbrella|flower|bag|tool)[^\s,.!?]*"],
            "only props explicitly requested in the original request",
        ),
        "setting_and_composition": first_match(
            request,
            [r"[^\s,.!?]*(?:배경|주방|방안|거실|공원|숲|해변|거리|카페|학교)[^\s,.!?]*", r"[^\s,.!?]*(?:background|kitchen|living room|park|forest|beach|street|cafe|school)[^\s,.!?]*"],
            "simple unobtrusive background; white when suitable",
        ),
    }


def prompt_skeleton(template: str) -> str:
    # Both project templates intentionally leave their final text block open.
    marker = "```text\n"
    if template.count(marker) != 1:
        raise ValueError("템플릿에서 프롬프트 골격을 찾을 수 없습니다.")
    return template.split(marker, 1)[1].removesuffix("```").strip()


def fill_template(skeleton: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        skeleton = skeleton.replace("{{" + key + "}}", value)
    remaining = re.findall(r"\{\{[^{}]+\}\}", skeleton)
    if remaining:
        raise ValueError(f"템플릿 항목이 채워지지 않았습니다: {remaining}")
    return skeleton


def latest_output() -> Path | None:
    images = [p for p in OUTPUT.glob("*.png") if p.is_file()]
    return max(images, key=lambda p: p.stat().st_mtime) if images else None


def is_edit(request: str, source: Path | None) -> bool:
    if source is not None:
        return True
    return bool(re.search(r"이 이미지|이 사진|기존 이미지|원본|이 그림|수정|고쳐|변경|바꿔|교체|제거|없애|삭제|편집", request))


def validate_source(path: Path) -> Path:
    path = path.expanduser().resolve()
    if not path.is_file() or path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
        raise ValueError(f"편집할 PNG, JPG 또는 WEBP 이미지가 필요합니다: {path}")
    if path.stat().st_size >= 50 * 1024 * 1024:
        raise ValueError("입력 이미지는 50MB 미만이어야 합니다.")
    return path


def prepare(request: str, source: Path | None) -> dict:
    # AGENTS.md: read the Character Lock first on every run.
    lock = read_required("style/MONGSIL_Character_Lock.md")
    read_required("AGENTS.md")
    edit = is_edit(request, source)
    template_name = "MONGSIL_Edit.md" if edit else "MONGSIL_Scene.md"
    template = read_required(f"templates/{template_name}")
    view = view_for(request)
    primary, secondary, details = select_references(request, view)
    interpreted = interpret(request, view)

    if edit:
        source = validate_source(source or latest_output() or Path("missing-image"))
        # Source image is always image input #1 and controls the edit.
        inputs = [source, *([primary] if source != primary.resolve() else []), *details]
        preserve = (
            "All areas and attributes not explicitly requested for change: face, head, "
            "body, markings, pose, camera, outfit, props, background, linework, and color."
        )
        values = {
            "requested_changes": request,
            "source_image": str(source),
            "edit_region": "Only the element or area explicitly named in the user's request",
            "preserve_list": preserve,
            "output_conditions": "One PNG image; preserve the original file unchanged.",
        }
    else:
        inputs = [primary, *([secondary] if secondary else []), *details]
        values = {
            "user_request": request,
            "primary_reference": f"Input image 1: {primary.name}",
            "secondary_reference_if_any": f"Input image 2: {secondary.name}" if secondary else "None needed",
            "setting_and_composition": interpreted["setting_and_composition"],
            "action_and_pose": interpreted["action_and_pose"],
            "expression": interpreted["expression"],
            "view": interpreted["view"],
            "outfit": interpreted["outfit"],
            "props": interpreted["props"],
            "output_conditions": "One clean PNG illustration.",
        }

    skeleton = fill_template(prompt_skeleton(template), values)
    prefix = (
        f"ORIGINAL USER REQUEST (authoritative for scene or requested edit):\n{request}\n\n"
        f"Input image order: {', '.join(p.name for p in inputs)}.\n"
        "Use these actual attached images as visual references in the stated priority.\n\n"
    )
    prompt = prefix + skeleton + "\n\nFULL CHARACTER LOCK (identity specification):\n" + lock
    if edit:
        prompt += (
            "\n\nEDIT PRIORITY: The user's explicitly requested change is an exception "
            "to the corresponding Character Lock feature. For example, an explicit "
            "tail removal must remove only the tail while preserving every other feature. "
            "Do not use the identity specification to undo the requested edit."
        )
    if len(prompt) > 32_000:
        raise ValueError("요청이 길어 이미지 API의 32,000자 프롬프트 제한을 넘었습니다.")
    return {
        "mode": "edit" if edit else "scene",
        "request": request,
        "template": template_name,
        "primary": source if edit else primary,
        "secondary": primary if edit and source != primary.resolve() else (None if edit else secondary),
        "details": details,
        "inputs": inputs,
        "interpreted": interpreted,
        "prompt": prompt,
    }


def run_api(plan: dict) -> tuple[bytes, str]:
    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY가 설정되지 않아 이미지 API를 호출하지 않았습니다.")
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise ValueError("OpenAI Python SDK가 없습니다. python3 -m pip install -r requirements.txt") from exc
    with ExitStack() as stack:
        image_files = [stack.enter_context(path.open("rb")) for path in plan["inputs"]]
        response = OpenAI().images.edit(
            model=MODEL,
            image=image_files,
            prompt=plan["prompt"],
            output_format="png",
            quality="high",
        )
    if not response.data or not response.data[0].b64_json:
        raise ValueError("이미지 API가 이미지 데이터를 반환하지 않았습니다.")
    return base64.b64decode(response.data[0].b64_json), getattr(response.data[0], "revised_prompt", None)


def save_result(plan: dict, image_bytes: bytes, revised_prompt: str | None) -> tuple[Path, Path]:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    base = f"mongsil-{plan['mode']}-{stamp}-{uuid4().hex[:8]}"
    image_path = OUTPUT / f"{base}.png"
    record_path = OUTPUT / f"{base}.json"
    record = {
        "created_at": datetime.now().astimezone().isoformat(),
        "model": MODEL,
        "mode": plan["mode"],
        "original_request": plan["request"],
        "template": plan["template"],
        "primary_reference": str(plan["primary"]),
        "secondary_reference": str(plan["secondary"]) if plan["secondary"] else None,
        "detail_references": [str(p) for p in plan["details"]],
        "image_inputs_in_order": [str(p) for p in plan["inputs"]],
        "interpreted_request": plan["interpreted"],
        "final_prompt": plan["prompt"],
        "api_revised_prompt": revised_prompt,
        "result_image": str(image_path),
    }
    # Exclusive creation protects existing outputs and source images.
    with image_path.open("xb") as file:
        file.write(image_bytes)
    with record_path.open("x", encoding="utf-8") as file:
        json.dump(record, file, ensure_ascii=False, indent=2)
        file.write("\n")
    return image_path, record_path


def main() -> int:
    parser = argparse.ArgumentParser(description="몽실이 자연어 이미지 생성·편집 실행기")
    parser.add_argument("request", nargs="*", help="몽실이에게 원하는 장면이나 수정 내용을 자연어로 입력")
    parser.add_argument("--image", type=Path, help="편집할 원본 이미지 경로. 생략하면 output/의 최근 이미지 사용")
    args = parser.parse_args()
    request = " ".join(args.request).strip() or input("몽실이에게 원하는 장면이나 수정 내용을 입력하세요: ").strip()
    if not request:
        parser.error("요청 내용을 입력하세요.")
    try:
        OUTPUT.mkdir(exist_ok=True)
        plan = prepare(request, args.image)
        print(f"작업: {'기존 이미지 편집' if plan['mode'] == 'edit' else '새 장면 생성'}")
        print(f"PRIMARY: {plan['primary']}")
        print(f"SECONDARY: {plan['secondary'] or '없음'}")
        if plan["details"]:
            print("DETAIL: " + ", ".join(str(p) for p in plan["details"]))
        if not os.environ.get("OPENAI_API_KEY"):
            print("OPENAI_API_KEY가 없어 실제 이미지 생성 호출을 하지 않았습니다.")
            return 0
        image_bytes, revised_prompt = run_api(plan)
        image_path, record_path = save_result(plan, image_bytes, revised_prompt)
        print(f"이미지: {image_path}")
        print(f"작업 기록: {record_path}")
        return 0
    except (ValueError, OSError) as exc:
        print(f"오류: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
