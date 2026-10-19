# 템플릿: 몽실이 장면 (MONGSIL Scene)

몽실이 이미지 프롬프트는 이 골격으로 만든다.
캐릭터 규칙의 원문은 `character/MONGSIL_Character_Lock.md`, 3D 렌더 규칙은 `styles/MONGSIL_3D_Felt.md`에 있다. 이 템플릿은 그 규칙을 **프롬프트 문장으로 옮기는 방법**만 정한다. 락 & 스타일 내용과 충돌하면 락 & 스타일이 이긴다.

---

## 1. 블록 선택표

장면에 필요한 블록만 넣는다. 필수 블록은 항상 넣는다.

| 블록 | 넣는 경우 | 필수 |
|---|---|---|
| Element 줄 | 항상 | ● |
| `## Subject` | 항상 | ● |
| `## Orientation` | 항상 (정면 기본 자세라도 한 줄은 쓴다) | ● |
| `## Pose & Paws` | 팔이나 다리가 기본 자세와 다를 때, 앞발로 무언가 할 때 | |
| `## Prop` | 소품이 있을 때 | |
| `## Wardrobe` | 모자, 옷, 액세서리가 있을 때 | |
| `## Environment` | 흰 배경이 아닐 때 | |
| `## Camera` | 항상 | ● |
| `## Style` | 항상 (3D는 아래 문장 그대로) | ● |
| `## Critical conditions` | 항상 | ● |
| `## Negative` | 항상 | ● |

빈 블록은 지운다. "없음"이라고 쓰지 않는다.

---

## 2. 프롬프트 골격

```
<<<몽실 Element ID>>> <<<소품 Element ID (있을 때만)>>> # {장면 제목}

## Subject
MONGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant almost-round head that is slightly wider than it is tall, full cheeks and a soft rounded lower face, a short rounded torso, short rounded limbs, and no visible neck.
Small black facial features as in the reference. Thin black whiskers that grow from the cheeks and extend beyond the face outline in space, matching the reference arrangement.
A brown #B79571 wave-shaped marking on MONGSIL's own left ear and upper head (screen right in front view). Inner ears #FFCDB4. Black features and whiskers #000000.
A centred, slightly vertical oval belly patch. Brown cloud-like tail and brown arm marking exactly where the reference shows them.
Expression: {표정}.

## Orientation
- Body faces: {몸 방향, 예: three-quarter toward screen left}
- Head faces: {머리 방향, 예: turned slightly more toward the camera than the body}
- Eyes look at: {시선 대상, 예: the gift box / the camera / off to screen right}
The head turns on the body naturally with no visible neck. The face, ears, and the brown wave marking rotate with the head; markings stay on MONGSIL's anatomical left side and never mirror.

## Pose & Paws
{자세 1~2문장. 팔 방향은 신체 기준과 화면 기준을 둘 다 쓴다.
예: MONGSIL's left arm (screen right) reaches forward; its right arm (screen left) rests at its side.}
Paws are short rounded nubs with no fingers. {앞발과 소품의 접촉 방식 — 아래 4번 참고}

## Prop
{소품 이름}: {형태, 색, 재질}. {소품 방향, 예: long side horizontal, the notch facing screen right}.
Size: {몽실 머리와 비교한 크기, 예: about half the width of MONGSIL's head}.
The prop keeps exactly this shape and orientation{소품 Element가 있으면: as in the prop reference}. Nothing is printed on it unless stated.

## Wardrobe
{의상 & 액세서리}. It sits on top of MONGSIL without changing the head shape, ears, or body volume, and does not cover the brown wave marking unless stated.

## Environment
{배경. 기본: clean light gray to white seamless studio background with a soft contact shadow.}

## Camera
{정면 & 3/4 & 측면 & 후면} view, eye level, {full body / waist up}, centred, nothing cropped.

## Style
Soft flocked felt 3D mascot figure with a very short, dense, even matte pile. Soft even studio lighting, gentle contact shadow. No long fur, no individual hairs, no seams or stitching, no glossy plastic or vinyl.

## Critical conditions (must all hold)
1. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
2. The head stays an almost-round oval slightly wider than it is tall — not a sphere, not a vertically long oval.
3. The brown wave marking stays connected to MONGSIL's left ear and upper head (screen right in front view), with its wave contour intact and not mirrored.
4. The belly patch is centred and a slight vertical oval, following the body surface — not a circle, not a button.
5. Whiskers grow from the cheeks and stand out in space — not printed, engraved, or pressed into the face.
6. Colours stay literal: brown #B79571, inner ears #FFCDB4, features #000000. No other pink is set to #FFCDB4 by assumption.
{7~. 이번 장면 고유 조건 — 소품 방향, 시선 대상, 앞발 접촉 등}

## Negative
{공통 Negative} + {장면 고유 Negative}
```

---

## 3. 시선 & 몸 방향 쓰는 법

- 몸 방향, 머리 방향, 시선 대상을 **따로 한 줄씩** 쓴다. 한 문장에 섞으면 모델이 전부 정면으로 맞춘다.
- "앞 & 뒤 & 왼쪽 & 오른쪽"은 신체 기준인지 화면 기준인지 항상 밝힌다. 둘 다 쓰는 게 가장 안전하다.
  - 실측: "팔을 앞뒤로" 지시가 2회 연속 반대로 나왔다 (`prompts/2026-10-01-mongsil-3d-walk-paw-pads.md`)
- 몸이 측면인데 얼굴만 정면으로 고정되는 실패가 있었다 (`prompts/2026-09-30-higgsfield-element-failures.md`). 몸과 머리를 다르게 원하면 각도 차이를 명시하고, 같게 원하면 "head and body face the same direction"을 쓴다.

## 4. 앞발 & 소품 상호작용

| 상호작용 | 문장 예시 |
|---|---|
| 두 손으로 들기 | holds the {prop} in front of its chest with both rounded paws pressed against the left and right sides of the {prop} |
| 한 손으로 들기 | holds the {prop} with its {left/right} paw (screen {right/left}); the paw wraps around the edge, no fingers |
| 끌어안기 | hugs the {prop} against its belly with both short arms; the paws rest on the front of the {prop} |
| 내밀기 | holds the {prop} out toward the camera at chest height with both paws underneath it |
| 누르기 & 터치 | touches the {prop} with the round tip of its {left/right} paw |

- 소품은 반드시 앞발에 **닿아 있게** 쓴다. 떠 있거나 몸에 붙어 있으면 안 된다.
- 소품이 배 패치를 다 가리면 4번 검증을 할 수 없다. 가려도 되는 장면이 아니면 "held low enough that part of the belly patch stays visible"을 넣는다.
- 손바닥 젤리가 보여야 하면 `@mongsil_3d_paw_front_v1`을, 발바닥이면 `@mongsil_3d_paw_hind_v1`을 소품 Element로 추가한다. 단, 앞발 젤리 개수는 Element & 숫자 지정 & Negative로도 보장되지 않았다 (실측 3회). 젤리가 중요한 컷이면 생성 전에 이 한계를 사용자에게 알린다.

## 5. 소품 형태 & 방향 유지

- 소품 Element가 있으면 Element 줄에 넣고, `## Prop`에도 형태를 글로 다시 쓴다 (Element + 글 이중 안전장치).
- 방향은 화면 기준으로 쓴다: 긴 변 가로 & 세로, 홈 & 절취선 위치, 기울기.
- 크기는 몽실 머리와 비교해서 쓴다. 숫자 cm 단위는 쓰지 않는다.
- 소품에 글자가 필요하면 `"..." rendered sharp, crisp, and clearly legible`. 필요 없으면 Negative에 `text on prop`.

## 6. 레퍼런스 & Element 조합

- 몽실 Element는 **1개만** 쓴다. 같은 캐릭터 Element를 여러 개 넣으면 여러 마리로 나온다.
- 몽실 1개 + 소품 Element 추가는 다중 캐릭터 문제를 만들지 않았다 (실측 2회).
- `@몽실3D_통합`은 정면 한 장만 주입된다. 정면이 아닌 구도는 `references/3d/`의 해당 각도 이미지를 `medias`로 함께 넣는다.
- 기존 결과를 고칠 때는 새로 생성하지 말고 그 결과를 편집 기준 이미지로 넣는다. 정체성 & 배경 & 질감이 잘 유지됐다 (실측 4회).

---

## 공통 Negative (항상 포함)

```
extra characters, two cats, duplicated MONGSIL, realistic cat, human body, long limbs, visible neck,
fingers, human hands, triangular face, pointed chin, narrow lower face, perfectly spherical head,
vertically long head, mirrored markings, brown marking on the wrong ear, missing ear wave marking,
simplified round brown patch, circular belly patch, horizontal oval belly patch, raised button belly,
whiskers printed on face, engraved whiskers, thick rigid whiskers, long fur, individual hairs,
fabric seams, stitching, glossy plastic, vinyl shine, clay render, text, watermark, logo,
cropped character, floating object
```

## 장면 고유 Negative 예시

- 소품 방향: `prop rotated, prop upside down, prop shape changed`
- 소품 접촉: `prop floating, prop not touching paws, prop fused into body`
- 시선: `looking at camera` (다른 곳을 봐야 할 때만)
- 의상: `hat covering the ear marking` (마킹이 보여야 할 때)

---

## 학습 루프

이 템플릿에서 고친 규칙은 `prompts/` 기록에서 **2회 이상 확인된 것만** 넣는다. 넣을 때 근거 기록 파일명을 함께 적는다.
락 & 스타일 파일 반영이 필요해 보이면 직접 고치지 말고 사용자에게 제안한다.
