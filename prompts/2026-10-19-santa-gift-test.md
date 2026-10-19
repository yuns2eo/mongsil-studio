# 산타 모자 & 선물상자 몽실이 (저장소 기준 첫 테스트)

- 날짜: 2026-10-19
- 요청(한국어): 몽실 저장소 기준으로, 산타 모자 쓰고 선물상자 들고 있는 몽실이 3D 이미지 만들어줘
- 상태: 미확인
- 모델 & 품질 & 해상도 & 비율: GPT Image 2 & low & 1K & 1:1
- Element: 몽실3D_통합 (26aee006-8db5-412e-8aa0-ef7aa61a312f)
- 첨부 레퍼런스: 없음
- job: 8a24db30-74cb-4841-b2a2-235d66a34d93
- 크레딧: 기록하지 않음 (크레딧 표시 규칙 추가 전 생성)

## 최종 프롬프트

```
<<<26aee006-8db5-412e-8aa0-ef7aa61a312f>>> standing upright, front view, slightly turned toward the viewer, wearing a small red Santa hat with white fur trim and a white pom-pom, tilted slightly on the head without covering the brown wave marking on the screen-right ear. Both short rounded arms hold a small red gift box with a gold ribbon bow in front of the chest, held low enough that the upper belly patch stays partly visible. Happy gentle expression.

Same exact character as the reference: almost-round head slightly wider than it is tall with full cheeks and a soft rounded lower face, small black dot eyes, tiny black nose, small w mouth, thin free-standing black whiskers extending from the cheeks beyond the face outline, soft pink cheek blush. Brown #B79571 wave-shaped marking on the screen-right ear and upper head, white screen-left ear with peach inner ear #FFCDB4, centered peach-pink vertical oval belly patch, brown cloud-shaped wavy tail behind, small brown arm marking as in the reference, short stubby legs.

Style: soft flocked felt 3D mascot figure, very short dense matte velvety pile, no long fur, no plastic shine, no seams. Soft even studio lighting, gentle contact shadow, clean light gray to white seamless background, cozy subtle Christmas mood. Centered full-body shot.

Do not: mirror or move the brown marking, simplify the ear wave into a blob, make a triangular or pointed lower face, make the belly patch a circle, print or engrave the whiskers flat on the face, add fingers, lengthen limbs, add extra characters, add text.
```

## 검증 (락 파일 9번)

| 항목 | 결과 |
|---|---|
| 1. 세모 옆얼굴 | 해당 없음 (정면) |
| 2. 머리 형태 | 통과. 살짝 가로로 넓은 둥근 형태 |
| 3. 귀 물결 무늬 | 통과. 화면 오른쪽 귀에 연결, 반전 없음 |
| 4. 배 패치 | 통과. 선물상자 아래로 세로 타원 일부 보임 |
| 5. 수염 | 주의. 볼에서 살짝 떠 있지만 얼굴에 붙은 느낌이 남음. 양쪽 2가닥으로 레퍼런스와 배열이 다름 |
| 6. HEX | 통과로 보임 (프롬프트에 리터럴 HEX 유지) |

## 실패 & 수정

- 수염 배열이 레퍼런스와 다름 → 원인 추정: 프롬프트에 개수를 쓰지 않았고(락 5번 규칙), 레퍼런스 정면 이미지가 엘리먼트로만 들어감 → 다음 시도 후보: `references/3d/Front.png`를 `medias`로 함께 첨부하고 "whisker arrangement matching the attached front reference" 지시 → 미시도
- 생성 기록에서 `몽실3D_통합`의 주입 이미지가 정면 1장뿐임을 확인 → README & CLAUDE.md & 템플릿에 반영함
- 프롬프트 형식이 템플릿 이전 버전(문단형) → 다음부터 `templates/mongsil-scene.md` 섹션형 사용

## 재사용 규칙

- 통합 Element는 첫 장만 주입된다 (생성 기록으로 확인, 1회)
- [x] 템플릿 반영 (6번 레퍼런스 & Element 조합)
- [ ] 락 & 스타일 반영 제안 (해당 없음)
