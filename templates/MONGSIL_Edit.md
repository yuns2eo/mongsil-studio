# MONGSIL Edit — 기존 이미지 편집 템플릿

## 목적

기존 몽실이 이미지에서 사용자가 지정한 일부 요소만 수정한다.

이 작업의 기본 원칙은:

> 변경 요청이 없는 영역은 다시 디자인하지 않는다.

편집은 새로운 몽실이를 다시 생성하는 작업이 아니다.

현재 이미지의 포즈, 구도, 캐릭터 모습, 스타일을 최대한 보존하면서
사용자가 지정한 부분만 최소 범위로 수정한다.


---

## 사용 시점

다음과 같은 요청에서 사용한다.

- 의상만 변경
- 소품 추가 / 제거 / 교체
- 표정만 변경
- 손이나 발 일부 수정
- 꼬리 추가 / 제거 / 수정
- 특정 패치 수정
- 현재 이미지의 일부 구조 오류 수정
- 배경 일부 수정

편집 대상 이미지가 없으면 먼저 해당 이미지를 받아야 한다.

편집 범위가 작을수록
가능한 경우 선택 영역 또는 마스크를 좁게 잡는다.


---

## 요청 해석

작업 전 다음을 명확하게 구분한다.

- 원본 이미지: `{{source_image}}`
- 바꿀 요소: `{{requested_changes}}`
- 반드시 유지할 요소: `{{preserve_list}}`
- 수정 영역: `{{edit_region}}`
- 출력 조건: `{{output_conditions}}`

사용자가 명시하지 않은 영역은 기본적으로 유지 대상이다.


---

## Reference Priority

기존 이미지 편집에서는 다음 순서를 따른다.

1. `{{source_image}}`
2. 해당 시점과 가장 가까운 공식 MONGSIL 턴어라운드
3. 필요한 경우 손 / 발 / 꼬리 상세 레퍼런스
4. `../style/MONGSIL_Character_Lock.md`
5. 사용자의 수정 요청


### 매우 중요

현재 편집 대상 이미지는:

- 포즈
- 구도
- 카메라
- 캐릭터 위치
- 크기
- 표정
- 기존 의상
- 기존 소품
- 선 스타일
- 채색
- 배경

의 PRIMARY visual reference다.

공식 턴어라운드와 Character Lock은
**편집해야 하는 부분의 캐릭터 정체성을 확인하기 위한 보조 기준**으로 사용한다.

사용자가 요청하지 않은 기존 차이나 오류를
공식 레퍼런스에 맞춘다는 이유로 자동 수정하지 않는다.

예:

사용자가

> "꼬리만 없애줘"

라고 요청했다면,

기존 이미지의 얼굴, 몸 비율, 팔다리, 의상, 표정 등이
공식 턴어라운드와 약간 다르더라도
그 부분은 수정 대상이 아니다.


---

## 편집 범위 원칙

### EDIT

사용자가 명시적으로 변경한 요소만 수정한다.

`{{requested_changes}}`


### PRESERVE

`{{preserve_list}}`에 포함된 요소는 최대한 그대로 유지한다.

또한 사용자가 별도로 언급하지 않은 영역도
기본적으로 유지한다.


### DO NOT REGENERATE

편집 대상과 관계없는 영역을
새로운 이미지처럼 다시 생성하지 않는다.

특히 다음 요소를 불필요하게 변경하지 않는다.

- 얼굴
- 머리 크기
- 몸 비율
- 귀
- 갈색 머리 패치
- 팔 무늬
- 배 패치
- 손발
- 꼬리
- 포즈
- 카메라 시점
- 의상
- 소품
- 배경
- 전체 선 스타일
- 색상
- 그림자

단, 이 중 사용자가 명시적으로 수정을 요청한 요소는 예외다.


---

## 꼬리 제거 예외

사용자가 명시적으로:

> "꼬리 없애줘"
> "꼬리 제거"
> "꼬리 삭제"

라고 요청하면 꼬리 제거를 허용한다.

이 경우:

- 꼬리만 제거한다.
- 꼬리가 있던 뒤쪽 몸 실루엣을 자연스럽게 복원한다.
- 허리, 엉덩이, 다리 구조를 새로 디자인하지 않는다.
- 다른 캐릭터 요소는 유지한다.

다른 요청에서는
Character Lock의 공식 꼬리 규칙을 따른다.


---

## 의상 편집

새 의상을 추가하거나 기존 의상을 변경할 경우:

의상을 몽실이의 기존 몸 위에 맞춘다.

몸을 의상에 맞추지 않는다.

유지:

- 기존 머리 크기
- 기존 몸 크기
- no-neck 구조
- 기존 팔 길이
- 기존 다리 길이
- 기존 손발 구조

금지:

- 의상 때문에 목 생성
- 어깨 생성
- 팔 길이 증가
- 다리 길이 증가
- 인간형 몸통 생성
- 인간형 골반 생성


---

## 소품 편집

새 소품을 추가할 경우:

소품을 몽실이의 현재 포즈와 짧은 앞발에 맞춘다.

가능하면:

- 소품 크기 조절
- 소품 위치 조절
- 손과 소품 일부 겹침
- 양손 지지

를 사용한다.

금지:

- 소품에 닿기 위해 팔 길이 늘리기
- 사람 손가락 만들기
- 손 전체를 인간 손처럼 재설계


---

## 부분 구조 수정

손, 발, 꼬리 등의 구조 자체를 수정하는 요청이면
해당 공식 detail reference를 사용할 수 있다.

예:

손바닥 수정
→ `MONGSIL_Paw_Inner.png`

발바닥 수정
→ `MONGSIL_Foot_Sole.png`

꼬리 수정
→ `MONGSIL_Tail.png`

해당 상세 레퍼런스는
수정 대상 부위에만 적용한다.

전체 캐릭터 비율이나 포즈를 바꾸는 기준으로 사용하지 않는다.


---

## 완성 편집 프롬프트 골격

```text
Edit the supplied MONGSIL image.

Make ONLY the following requested changes:

{{requested_changes}}

SOURCE IMAGE:
{{source_image}}

EDIT REGION:
{{edit_region}}

PRESERVE:
{{preserve_list}}

Everything outside the requested edit should remain visually unchanged wherever possible.

The supplied source image is the PRIMARY reference for pose, composition, camera angle, character placement, expression, existing outfit, existing props, linework, coloring, and background.

Use the official MONGSIL turnaround references and MONGSIL Character Identity Lock only to preserve character identity inside areas that must actually be redrawn.

Do NOT automatically correct unrelated differences between the current source image and the official turnaround.

Keep the same MONGSIL character and preserve the existing:
- head-to-body relationship
- compact body
- no-visible-neck construction
- short arms and legs
- simplified paws and feet
- facial identity
- fixed physical-side markings
- 2D linework and coloring

If adding clothing:
wrap the clothing around the existing MONGSIL anatomy.

If adding a prop:
adapt the prop to the existing paw and pose.

Do not redesign anatomy to solve the edit.

Do not regenerate unaffected areas.

AVOID:
changes outside the requested edit region,
unrequested face changes,
unrequested pose changes,
unrequested body-proportion changes,
long limbs,
human shoulders,
visible human-like neck,
human fingers,
mirrored or duplicated markings,
unintended tail changes,
inconsistent outline,
different coloring,
different shading,
3D rendering,
realistic texture,
full-image redesign.

OUTPUT:
{{output_conditions}}