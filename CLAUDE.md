# 몽실이(MONGSIL) 작업 규칙 — Claude Code용

이 폴더를 열면 이 파일이 자동으로 로드된다.
기본 운영 규칙은 `AGENTS.md`에 있다. **작업 전에 `AGENTS.md`를 먼저 읽고 그대로 따른다.**
이 파일은 Claude Code와 Higgsfield에서만 필요한 내용을 추가한다.

---

## 0. 절대 규칙

1. **사용자가 명시적으로 요청하기 전에는 이미지를 생성하지 않는다.** 프롬프트와 레퍼런스 선택까지만 준비한다.
2. 베이스 캐릭터를 새로 그리지 않는다. 턴어라운드, 3D, 승인 포즈는 모두 사용자가 완성한 원본이다.
3. 소품(들기, 먹기 등)은 기본 캐릭터에 포함되지 않는다. 기본 자세 변형(뛰기, 걷기, 눕기, 돌기 등)이 먼저이고 소품은 나중에 사물로 추가한다.
4. `references/`, `style/` 파일은 사용자 승인 없이 수정하거나 덮어쓰지 않는다.
5. 답변은 한국어로 한다. 가운뎃점(·) 대신 &를 쓴다.

---

## 1. 2D 라인과 3D 라인을 구분한다

몽실이는 렌더 스타일이 다른 두 라인이 있다. 요청이 어느 쪽인지 먼저 판단하고, 애매하면 사용자에게 묻는다.

| | 2D 라인 | 3D 라인 |
|---|---|---|
| 락 파일 | `style/MONGSIL_Character_Lock.md` | `style/MONGSIL_3D_Character_Lock.md` |
| 턴어라운드 | `references/MONGSIL_*.png` | `references/3d/MONGSIL_3D_*.png` |
| 승인 포즈 | `references/poses/` | `references/3d/MONGSIL_3D_Tongue.png`, `MONGSIL_3D_Sit.png` |
| 스타일 | 깔끔한 선 & 플랫 채색 일러스트 | 짧은 털 & 매트한 소프트 3D |

- 2D 락의 23번(3D 렌더 금지)은 2D 라인에만 적용한다.
- 두 라인의 레퍼런스를 한 생성에 섞지 않는다.

---

## 1-1. 승인 마스터 (APPROVED MASTER)

`masters/`에는 사용자가 직접 수정 & 승인한 최종 기준 이미지가 있다. 자세한 내용은 `masters/README.md`.

| 포즈 | 파일 |
|---|---|
| 3D 정면 점프 (양팔 들고 웃음) | `masters/MONGSIL_3D_Jump_APPROVED_MASTER.png` (원본 PNG 2883×2883). 같은 이름의 `.webp`는 압축 사본이라 제작용에서 제외 |

- 해당 포즈를 수정하거나 다시 만들 때는 **반드시 승인 마스터에서 시작**한다.
- 이전 생성물을 편집 기준으로 반복 재입력하지 않는다. 화질 & 디테일이 열화된다.
- 마스터에 있는 무늬 위치 & 크기 & 실루엣은 픽셀 그대로가 기준이다. 새로 해석 & 재디자인 & 추측하지 않는다.
- 승인 마스터는 사용자 승인 없이 수정하거나 덮어쓰지 않는다.

---

## 2. Higgsfield 엘리먼트

`.mcp.json`으로 Higgsfield MCP가 연결된다. 등록된 몽실이 엘리먼트는 아래와 같다.

### 3D 라인 (2026-10 등록)

| 엘리먼트 이름 | ID | 원본 |
|---|---|---|
| mongsil_3d_front_v1 | 250f17e2-f6d5-4bee-bc98-ac9703ab0e50 | `references/3d/MONGSIL_3D_Front.png` |
| mongsil_3d_left45_v1 | dcebd8eb-68ac-4396-bb1a-6942c110481a | `references/3d/MONGSIL_3D_Left_3Q.png` |
| mongsil_3d_leftside_v1 | 160af8e8-6755-4907-b253-79b37104874f | `references/3d/MONGSIL_3D_Left_Profile.png` |
| mongsil_3d_back_v1 | 745cd0c9-5be2-4338-b78d-a1d891e8f7d1 | `references/3d/MONGSIL_3D_Back.png` |
| mongsil_3d_paw_front_v1 (prop) | 2dd05d50-0962-4630-87c4-a27bfef1113d | `references/3d/MONGSIL_3D_Paw_Inner.png` |
| mongsil_3d_paw_hind_v1 (prop) | be4bcdd3-94c3-4d11-81b7-93e557e53060 | `references/3d/MONGSIL_3D_Foot_Sole.png` |
| mongsil_3d_tongue_v1 | ca55bb85-fc26-42bb-aa92-1e17f75d5439 | `references/3d/MONGSIL_3D_Tongue.png` |
| mongsil_3d_sit_v1 | ac3a7bf4-bc07-4300-9d1f-93c7b05d4528 | `references/3d/MONGSIL_3D_Sit.png` |

### 2D 라인

`mongsil_basic_front_v1`, `mongsil_basic_left45_v1`, `mongsil_basic_leftside_v1`, `mongsil_basic_back_v1`, `mongsil_paw_front_v1`, `mongsil_paw_hind_v1`, `mongsil_tail_v1`, `mongsil_master_v2` (bd066bd8-0e69-4053-a7e6-9b04ce2a781f)

- 예전 `MONGSIL` 엘리먼트(ea5bb845-…)는 이미지가 1장뿐인 구버전이다. 사용하지 않는다.

### 엘리먼트 사용 규칙 (실패로 확인된 내용)

- **한 생성에 몽실이 엘리먼트는 1개만 넣는다.** 같은 캐릭터 엘리먼트를 여러 개 넣으면 모델이 여러 마리로 읽는다.
- MCP로 만든 엘리먼트는 **첫 번째 이미지만** 생성에 주입된다. 그래서 엘리먼트 하나에 이미지 한 장씩 등록했다.
- 카메라 시점에 가장 가까운 엘리먼트 1개를 고른다. 다른 시점 확인이 필요하면 엘리먼트가 아니라 프롬프트 텍스트로 보완한다.
- 캐릭터에 고정되는 것은 엘리먼트에, 바뀌는 것(자세, 표정, 배경)은 프롬프트에 둔다.

### 생성 결과 검수

- 생성 결과는 Higgsfield MCP가 반환한 이미지 & 위젯(`show_generation_by_ids`, `job_display` 등) 기준으로 확인한다.
- 결과의 외부 CloudFront URL을 curl 등으로 직접 다운로드해서 검수하지 않는다.
- 네트워크 정책 때문에 URL 다운로드가 실패해도 생성 실패로 취급하지 않는다. 생성 성공 여부는 MCP가 반환한 job 상태(`completed`)로 판단한다.

---

## 3. 프롬프트 구조 (허들링 방식)

짧게 쓰고 블록으로 나눈다.

```
#Element      사용할 엘리먼트 1개
#Scene        한 줄 요약
#Subject      자세 & 표정 (소품 없음이 기본)
#Environment  배경 (기본: 흰 배경 또는 단순 배경)
#Style        2D 또는 3D 라인 스타일
#Composition  카메라 시점 & 거리
#Critical     지켜야 할 정체성 3가지: 머리 형태, 갈색 머리 패치, 오른팔 갈색 무늬
#Negative     긴 팔다리, 목, 사람 손, 무늬 반전, 추가 캐릭터
```

단계별로 쌓는다: 캐릭터 자세 확인 → 소품 추가 → 장면 추가.

---

## 4. 학습 루프

- 결과가 틀려서 고쳤다면 원인과 해결을 `prompts/`에 기록한다. 형식은 `AGENTS.md` 18번을 따른다.
- 반복해서 확인된 규칙만 이 파일이나 락 파일에 반영 제안한다. 락 파일은 사용자 승인 후에만 수정한다.
- 작업 시작 전 `git pull`, 규칙을 고쳤으면 커밋 & 푸시.
