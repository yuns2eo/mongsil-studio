# mongsil-studio

몽실이(MONGSIL) 캐릭터 이미지를 **언제 생성하든 같은 캐릭터로** 유지하기 위한 작업 기준 저장소입니다.

AI(Claude, ChatGPT, Codex 등)가 이 저장소의 규칙과 레퍼런스를 읽고 몽실이 작업을 합니다.

- Claude Code: 폴더를 열면 `CLAUDE.md`가 자동으로 로드됩니다.
- Codex: `AGENTS.md`를 읽습니다.
- 그 외 AI: 이 저장소의 락 파일과 레퍼런스 이미지를 첨부해서 요청합니다.

---

## 구조

```
CLAUDE.md                         Claude Code 규칙 & Higgsfield 엘리먼트 목록
AGENTS.md                         기본 운영 규칙 (모든 AI 공통)
style/
  MONGSIL_Character_Lock.md       2D 라인 아이덴티티 락 v2
  MONGSIL_3D_Character_Lock.md    3D 라인 아이덴티티 락
templates/
  MONGSIL_Scene.md                새 장면 생성 템플릿
  MONGSIL_Edit.md                 기존 이미지 편집 템플릿
references/
  MONGSIL_Front / Left_3Q / Left_Profile / Back.png   2D 턴어라운드
  MONGSIL_Paw_Inner / Foot_Sole / Tail.png            2D 상세
  poses/                                              2D 승인 포즈
  3d/
    MONGSIL_3D_Front / Left_3Q / Left_Profile / Back.png   3D 턴어라운드
    MONGSIL_3D_Paw_Inner / Foot_Sole.png                   3D 상세
    MONGSIL_3D_Tongue / Sit.png                            3D 승인 포즈
prompts/                          검증된 프롬프트 & 실패 기록
mongsil.py                        자연어 요청 → 레퍼런스 선택 & 프롬프트 CLI
.mcp.json                         Higgsfield MCP 자동 연결
```

## 3D 원본과 Figma 레이어 대응

| 파일 | Figma 레이어 |
|---|---|
| MONGSIL_3D_Front.png | 몽실_정면 |
| MONGSIL_3D_Left_3Q.png | 몽실_45도 |
| MONGSIL_3D_Left_Profile.png | 몽실_측면 |
| MONGSIL_3D_Back.png | 몽실_후면 |
| MONGSIL_3D_Paw_Inner.png | 몽실_앞발 |
| MONGSIL_3D_Foot_Sole.png | 몽실_뒷발 |
| MONGSIL_3D_Tongue.png | 몽실_메롱 |
| MONGSIL_3D_Sit.png | 몽실_앉기 |

## 우선순위

충돌하면 위쪽이 이깁니다.

1. 공식 레퍼런스 이미지
2. 락 파일 (2D 또는 3D)
3. 사용자의 자세 & 장면 요청
4. 소품 & 배경

## 사용법

```
git clone <이 저장소>
cd mongsil-studio
claude
```

그다음 한국어로 요청합니다.

```
3D 몽실이가 걷는 모습 프롬프트 만들어줘
2D 몽실이 누워있는 자세, 흰 배경
```

## 규칙

- 작업 시작 전 `git pull`
- 결과가 틀려서 고쳤으면 `prompts/`에 기록하고 커밋 & 푸시
- `references/`와 `style/`은 승인 없이 수정하지 않기
- 이 저장소는 **Private**로 유지
