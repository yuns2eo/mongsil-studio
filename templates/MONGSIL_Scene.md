# MONGSIL Scene — 새 장면 생성 템플릿

## 목적

기존 오리지널 캐릭터 MONGSIL을
새로운 포즈, 행동, 의상, 소품, 환경에 배치하는 새 이미지 생성용 템플릿이다.

이 작업은 새로운 고양이 캐릭터를 디자인하는 작업이 아니다.

항상:

> same MONGSIL + new scene

으로 처리한다.


---

## 사용 시점

사용자가 다음과 같이 새로운 몽실이 장면을 요청했을 때 사용한다.

예:

- "몽실이가 사과를 들고 뛰는 모습"
- "몽실이가 셰프복 입고 요리하는 장면"
- "몽실이가 스마트폰으로 QR 코드를 찍는 모습"
- "몽실이가 의자에 앉아서 책을 읽는 모습"

사용자에게 몽실이 외형을 다시 설명하도록 요구하지 않는다.

프로젝트의 공식 reference와 Character Lock을 자동으로 사용한다.


---

## 요청 해석

사용자의 자연어 요청에서 다음 항목을 내부적으로 정리한다.

- 원문: `{{user_request}}`
- 행동·포즈: `{{action_and_pose}}`
- 표정: `{{expression_or_natural_default}}`
- 카메라 시점: `{{view_or_best_view_for_action}}`
- 의상: `{{outfit_or_none}}`
- 소품: `{{props_or_none}}`
- 배경·구도: `{{setting_and_composition_or_simple_default}}`
- 출력 조건: `{{output_conditions}}`

치환이 끝난 최종 프롬프트에는 `{{...}}` placeholder를 남기지 않는다.


---

## 기본 해석 원칙

사용자가 명시하지 않은 다음 요소는 임의로 추가하지 않는다.

- 의상
- 모자
- 액세서리
- 장식
- 소품
- 텍스트
- 로고
- 추가 캐릭터
- 추가 동물
- 복잡한 배경 요소

장면을 성립시키는 데 꼭 필요한 최소한의 요소만 추가한다.


### 표정

표정이 지정되지 않았다면
장면에 자연스럽게 맞는 기본 표정을 사용한다.

과장된 표정을 임의로 만들지 않는다.


### 배경

배경이 지정되지 않았다면
캐릭터와 행동을 명확하게 보여줄 수 있는
단순하고 방해되지 않는 배경을 사용한다.

캐릭터 테스트 성격의 이미지에서는
가능하면 흰색 또는 매우 단순한 배경을 우선한다.


### 카메라 시점

카메라 시점이 지정되지 않았다면:

1. 행동을 가장 자연스럽게 보여주는 시점을 선택한다.
2. 동시에 몽실이의 정체성이 잘 보이는 시점을 선호한다.
3. 특별한 이유가 없으면 정면 또는 약한 3/4 시점을 우선한다.


---

# Reference Selection

## 먼저 EDIT 가능성 판단

`../references/poses/`에서 사용자 행동과 충분히 가까운 승인 포즈를 찾는다. 소품, 의상, 표정 또는 작은 자세 수정만으로 요청을 구현할 수 있으면 새 이미지를 처음부터 만들지 않는다. 해당 승인 포즈 복사본을 source image로 삼고 `MONGSIL_Edit.md` 흐름으로 전환한다. 공식 턴어라운드는 캐릭터 정체성 확인에 사용한다.

승인 포즈가 없거나 큰 자세 재구성이 필요할 때만 이 NEW SCENE 템플릿을 계속 사용한다.

## IDENTITY REFERENCE

카메라 시점에 가장 가까운 공식 Front / Left 3Q / Left Profile / Back 턴어라운드를 선택한다. 이 이미지는 얼굴, 무늬, 기본 체형과 비율, 3차원 정체성을 결정한다. 아래 PRIMARY / SECONDARY 선택 규칙에 따라 실제 이미지를 사용한다.

## POSE REFERENCE

`../references/poses/`에서 행동이 가장 가까운 승인 포즈를 별도로 찾는다. 사용할 만한 포즈가 있으면 팔·다리 위치, 몸 실루엣, 앞발 사용 방식, 몸의 압축과 회전, 동작 중 비율을 이 이미지에서 우선 참고한다. 포즈 레퍼런스는 턴어라운드의 캐릭터 정체성 역할을 대체하지 않는다.

카메라 시점만 보고 턴어라운드 한 장으로 자세를 처음부터 상상하지 않는다. 승인 포즈와 요청 사이의 차이가 작으면 위 EDIT 판단으로 돌아간다. 적절한 포즈가 없으면 `POSE REFERENCE: 없음`으로 기록하고 새 자세를 생성한다.

## 출력 형식

```text
[작업 방식]
EDIT 또는 NEW SCENE

[IDENTITY REFERENCE]
선택한 공식 턴어라운드

[POSE REFERENCE]
선택한 승인 포즈 또는 없음

[DETAIL REFERENCE]
필요한 상세 이미지 또는 없음

[최종 이미지 생성/편집 프롬프트]
완성된 프롬프트
```

현재는 이미지 API를 실행하지 않고 이 선택 결과와 프롬프트를 제공한다.

## 1. Character Lock

모든 작업에서 먼저 다음을 적용한다.

`../style/MONGSIL_Character_Lock.md`

사용자의 요청이 짧아도 Character Lock 적용을 생략하지 않는다.


## 2. PRIMARY visual reference

다음 공식 턴어라운드 중
요청된 카메라 시점에 가장 가까운 한 장을 PRIMARY reference로 선택한다.

- `../references/MONGSIL_Front.png`
- `../references/MONGSIL_Left_3Q.png`
- `../references/MONGSIL_Left_Profile.png`
- `../references/MONGSIL_Back.png`

기본 선택:

### Front
PRIMARY:
`MONGSIL_Front.png`

### Weak / normal 3/4
PRIMARY:
`MONGSIL_Left_3Q.png`

### Profile
PRIMARY:
`MONGSIL_Left_Profile.png`

### Back
PRIMARY:
`MONGSIL_Back.png`


## 3. SECONDARY visual reference

필요한 경우에만
인접 시점 한 장을 SECONDARY reference로 추가한다.

SECONDARY는:

- 회전 구조 확인
- 반대쪽 형태 확인
- 비대칭 특징의 물리적 위치 확인

용도로만 사용한다.

PRIMARY와 동일한 가중치로 사용하지 않는다.


## 4. Detail references

다음 부위가 실제 장면에서 중요하게 보일 때만
존재하는 detail reference를 추가한다.

- 손바닥
- 발바닥
- 꼬리

예:

손바닥이 카메라를 향함
→ Paw Inner reference

발바닥이 크게 노출됨
→ Foot Sole reference

꼬리 구조가 중요하게 보임
→ Tail reference

보이지 않는 부위를 억지로 노출하지 않는다.


---

# Actual Reference Usage

이미지 생성 도구가 reference image 입력을 지원하는 경우:

공식 레퍼런스를 단순히 프롬프트 안에서 언급하는 것으로 끝내지 않는다.

반드시 실제 이미지 생성 요청에:

1. PRIMARY reference
2. 필요한 경우 SECONDARY reference
3. 필요한 경우 detail reference

를 실제 이미지 입력으로 전달한다.

공식 reference가 존재하는데
텍스트 설명만으로 몽실이를 새로 재구성하지 않는다.


---

# Reference Priority

시각적 구조가 충돌할 경우 다음 우선순위를 따른다.

1. 공식 PRIMARY MONGSIL reference
2. 공식 SECONDARY / detail references
3. MONGSIL Character Lock
4. 사용자의 pose / scene 요청
5. 배경 및 장식 요소

공식 reference의 실제 형태가
텍스트 설명보다 더 정확하다면
공식 reference를 따른다.


---

# Identity Lock

새로운 장면에서도 다음은 고정한다.

- 큰 둥근 머리
- 충분한 볼륨의 짧고 컴팩트한 몸
- distinct neck 없음
- 매우 짧고 통통한 팔
- 매우 짧은 다리
- 단순한 둥근 앞발
- 단순한 둥근 발
- 작은 중앙 집중형 얼굴
- 고정된 갈색 머리 패치
- 정확히 한쪽 팔의 갈색 무늬
- 앞면에서 보이는 복숭아색 배 패치
- 두껍고 구름처럼 둥근 갈색 꼬리
- 공식 2D 일러스트 스타일


---

# Asymmetric Identity Rule

몽실이의 비대칭 특징은
화면 좌우가 아니라 실제 신체 기준으로 유지한다.

특히:

- 갈색 머리 패치
- 한쪽 팔의 갈색 무늬

는 카메라가 회전하거나 캐릭터가 반대 방향을 바라보더라도
동일한 physical side에 남아 있어야 한다.

금지:

- 화면 좌우가 바뀌었다고 패치 위치를 미러링
- 대칭을 위해 양팔에 갈색 무늬 생성
- 머리 패치를 반대 귀 쪽으로 이동

MONGSIL은 하나의 일관된 3D 캐릭터가 회전하는 것으로 생각한다.


---

# Pose Construction Rule

포즈는 자유롭게 바뀔 수 있다.

허용:

- rotation
- bending
- overlap
- foreshortening
- squash
- perspective compression
- body tilt

하지만 캐릭터의 기본 신체 길이는 바꾸지 않는다.


## 절대 금지

- 팔을 소품까지 늘리기
- 달리기 때문에 다리 길게 만들기
- 앉는 자세 때문에 인간형 골반 만들기
- 손을 쓰기 위해 사람 손가락 만들기
- 의상 때문에 목 생성
- 활동적인 포즈 때문에 인간형 관절 생성


## 어려운 포즈 해결 순서

포즈 구현이 어렵다면 다음을 먼저 조정한다.

1. 몸의 회전
2. 카메라 각도
3. 단축원근
4. 팔·다리의 겹침
5. 소품 위치
6. 소품 크기
7. 몸 기울기
8. 구도

팔다리 길이 증가는 해결 방법으로 사용하지 않는다.


---

# Outfit Rule

의상은 기존 MONGSIL 몸 위에 입힌다.

의상이 몽실이의 체형을 바꾸면 안 된다.

금지:

- human shoulders
- visible neck
- narrow waist
- human torso
- long sleeves implying long arms
- long trousers implying long legs
- human hips

일반적인 의상이 몽실이 체형에 맞지 않는 경우:

몽실이를 변형하지 말고
의상을 단순화한다.


---

# Prop Rule

소품은 몽실이의 기존 짧고 둥근 앞발에 맞춘다.

필요하면:

- 소품을 조금 작게 조정
- 소품을 몸 가까이에 배치
- 양손으로 지지
- 몸에 기대기
- 손과 소품을 자연스럽게 겹치기

를 사용한다.

금지:

- 소품에 닿기 위해 팔 늘리기
- 인간형 grip 생성
- human fingers 생성


---

# Visibility Rule

카메라와 포즈상 보이지 않는 특징은
억지로 보여주지 않는다.

예:

- 옷에 가려진 belly patch
- 뒤쪽으로 돌아간 arm marking
- 카메라 반대쪽 paw pads
- 바닥을 향한 foot soles

특징을 유지한다는 것은
항상 화면에 보여야 한다는 뜻이 아니다.

같은 물리적 캐릭터 위에 존재하면 된다.


---

# 완성 프롬프트 골격

```text
Create a new 2D illustration of the existing original character MONGSIL.

This is NOT a redesign and NOT a new cat inspired by MONGSIL.
It is the exact same existing MONGSIL character placed into a new scene.

PRIMARY VISUAL REFERENCE:
{{primary_reference}}

SECONDARY VISUAL REFERENCE:
{{secondary_reference_if_any}}

Follow the official MONGSIL turnaround references and MONGSIL Character Identity Lock v2.

The PRIMARY reference controls the character geometry for this camera view.
Use the SECONDARY reference only to support three-dimensional rotation and identity.

If written instructions and the official visual reference differ in a minor structural detail, preserve the official visual reference.

SCENE:
{{setting_and_composition}}

ACTION AND POSE:
{{action_and_pose}}

EXPRESSION:
{{expression}}

CAMERA VIEW:
{{view}}

OUTFIT:
{{outfit}}

PROPS:
{{props}}

OUTPUT:
{{output_conditions}}

CHARACTER IDENTITY — PRESERVE:

- the same large rounded MONGSIL head
- the same substantial compact torso
- no distinct visible neck
- very short thick arms
- extremely short legs
- simple rounded paws and feet
- small centralized facial features
- the same fixed physical-side brown head marking
- exactly one brown arm marking on the correct physical arm
- centered peach belly marking when naturally visible
- the same thick cloud-like brown tail attached at the lower back
- the same official clean 2D illustration style

POSE RULE:

Perform the requested action through rotation, bending, overlap, body tilt, and foreshortening.

Do NOT increase the underlying anatomical length of the arms or legs.

If the action is difficult, adjust the camera, prop position, overlap, or composition instead of changing MONGSIL's anatomy.

OUTFIT RULE:

Clothing wraps around MONGSIL's existing body.

Do not reshape MONGSIL to fit human clothing.

PROP RULE:

Place props within natural reach of the existing short rounded paws.

Adapt the prop to MONGSIL instead of adapting MONGSIL to the prop.

ASYMMETRY RULE:

Track the brown head patch and single-arm marking by physical body side, not by screen-left or screen-right.

Do not mirror fixed markings when the character rotates.

VISIBILITY RULE:

Do not force hidden belly markings, paw pads, sole details, or hidden arm markings into view.

AVOID:

new cat design,
humanoid anatomy,
visible neck,
human shoulders,
narrow human torso,
long arms,
long legs,
human fingers,
realistic joints,
altered head-to-body proportions,
mirrored head marking,
duplicated arm marking,
brown markings on both arms,
generic thin cat tail,
tail attached to thigh or side hip,
extra paw pads,
oversized anime eyes,
realistic fur,
3D toy rendering,
clay rendering,
glossy plastic,
photorealistic texture,
unrequested clothing,
unrequested accessories,
unrequested text,
unrequested logo,
unrequested extra characters.
