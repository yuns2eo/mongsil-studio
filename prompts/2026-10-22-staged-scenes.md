# 단계별 장면 생성 (수의사 & 장바구니 & 택배기사)

- 날짜: 2026-10-22
- 모델 & 품질 & 해상도: GPT Image 2 & low & 1K (전 컷 공통, 1장씩)
- Element: 몽실3D (`665f4833-d075-4ac0-8f6e-2eaa0c18a3b5`)
- 첨부 레퍼런스: 아래 표의 `medias` 참고
- 크레딧: 컷당 0.5. 마지막 조회 기준 남은 203

## 컷별 결과

| 컷 | 요청(한국어) | job | medias | 비율 | 상태 |
|---|---|---|---|---|---|
| 수의사 STEP 1 | 의사 가운을 입은 몽실이 (의상 & 소품) | `2d8cca62-4f41-4c43-8974-94934c39a817` | 없음 | 1:1 | 승인 |
| 수의사 STEP 2 | 동물 병원에서 강아지를 진찰하는 장면 | `25861486-37f8-4d44-a2d8-acd9bcd53753` | STEP 1 job | 4:3 | 실패 (몸이 책상 위에 올려진 것처럼 보임) |
| 수의사 STEP 2 편집 | 책상 뒤에 서서 숙인 자세로 깊이만 수정 | `d66a7a7b-b605-40db-b1a3-de7e80d9eecb` | STEP 2 job | 4:3 | 실패 (깊이 문제 그대로, 반복 편집으로 화질 저하) |
| 수의사 STEP 2 신규 | 같은 장면을 원본 Element로 새로 생성 | `a20452df-493e-42ca-8760-fbfef6d3312e` | 없음 | 4:3 | 승인 |
| 장바구니 STEP 1 | 돋보기 들고 한쪽 눈 찡긋 | `1e460145-5734-4055-bdd4-945316d5db73` | 없음 | 1:1 | 미확인 (다음 단계 진행 요청) |
| 장바구니 STEP 2 | 빨간 장바구니 너머로 들여다보기 | `6a713ff3-7c35-4502-8813-d7496b33cacb` | STEP 1 job | 1:1 | 미확인 |
| 창고 STEP 1 | 상자를 머리 위로 번쩍 들기 | `14df4313-4f3c-4e11-b668-c7d27332cc51` | 없음 | 1:1 | 실패 (팔이 얼굴에 붙고 길어짐) |
| 창고 STEP 1 v2 | 상자를 가슴 앞에 끌어안기, 45도 | `38ab0730-f2bd-49ce-9cf1-3b0f39d45dba` | 없음 | 1:1 | 실패 (배 패치 가려짐, 팔 무늬 하트 모양) |
| 창고 STEP 1 v3 | 핑크 택배 모자 & 열린 조끼, 팔 무늬 빼기 | `199a2a3f-cf98-4fda-a487-7376c7b91379` | 없음 | 1:1 | 실패 (디테일 부족) |
| 택배기사 STEP 1 v4 | 남색 카라티 & 핑크 모자 & 발바닥 마크, 믿음직한 표정 | `d4eae467-c187-400e-b67b-9680f58287de` | 없음 | 1:1 | 승인 (모자 색 & 상자는 다른 AI로 수정 예정) |

## 최종 프롬프트 (승인 컷 중 대표: 수의사 STEP 2 신규)

```
<<<665f4833-d075-4ac0-8f6e-2eaa0c18a3b5>>>
#Scene: A cozy, bright animal hospital exam room. Mongsil works as a veterinarian, gently examining a small cream-colored fluffy puppy plush with a stethoscope.
#Subject: White doctor's coat with a chest pocket, thin round metal glasses, light-blue stethoscope. Mongsil STANDS ON THE FLOOR BEHIND the white exam table and leans the upper body forward over it.
#Environment: White exam table with a pink mat in the foreground. Window on the left, pastel shelves, cabinets and a sink on the right.
#Composition: 4:3, eye-level medium close-up. Mongsil left-center, puppy on the right.
#Critical: DEPTH: the exam table is IN FRONT of Mongsil; its back edge runs in front of Mongsil's waist and hides the lower body. Mongsil does NOT sit or rest on the tabletop; no body shadow on the tabletop. Head nearly circular oval, not triangular.
#Negative: upper body placed on the table, floating body, triangle face, slim body, long arms, extra brown spots, text, logo.
```

## 실패 & 수정

- 몸이 책상 위에 올려진 것처럼 보임 → 깊이 관계를 지정하지 않음 (확인) → `DEPTH` 문장을 Critical에 넣고 원본 Element로 새로 생성 → 해결
- 편집을 이어서 할수록 화질 저하 → 같은 결과를 반복 편집 (확인, 사용자 지적 2회: 만세 & 수의사) → 편집 1회까지, 이후 새로 생성 → 해결
- 상자를 머리 위로 들면 팔이 얼굴에 붙고 길어짐 → 짧은 팔로 무리한 자세 (확인 1회) → 끌어안기 자세로 변경 → 해결
- 손 흔드는 손바닥에 패드 없음 → 프롬프트에 패드 문장 누락 (확인) → 손바닥이 보이는 자세면 패드 문장 자동 포함 → 템플릿 반영
- 옷이 배 패치를 가림 → 상자 & 옷 위치 미지정 (확인) → 열린 조끼 & 짧은 상의 & 상자 낮게 들기 → 해결
- 팔 무늬가 하트 모양으로 나옴 → 형태 미지정 (추정) → 락 파일에 반쪽 구름 형태 명시

## 재사용 규칙

- 단계별 생성 (STEP 1 의상 & 소품 → STEP 2 장면 → STEP 3 합성): 사용자 지시
- 반복 편집 금지, 편집 1회까지: 2회 확인
- 앞 물체 깊이 문장: 1회 확인
- 손바닥 패드 문장 자동 포함: 사용자 지시
- [x] 템플릿 반영 (`templates/mongsil-scene.md` 4번 & 6번 & 7번)
- [x] 락 반영 (사용자 승인, 2026-10-22)
