# Tic Tac Toe

틱택토 게임은 Python을 사용하여 콘솔 환경에서 즐길 수 있는 간단한 게임입니다. 이 프로젝트는 2인용 또는 플레이어 대 AI 모드로 제공되며, Python의 기초적인 프로그래밍 기술을 연습할 수 있는 훌륭한 과제입니다.

---

## 주요 기능

- **플레이어 대 플레이어**: 두 명의 플레이어가 번갈아가며 "X"와 "O"를 선택하여 게임 진행.
- **플레이어 대 AI**: AI와 플레이어 간 대결. AI는 기본적인 승리 전략을 사용하여 게임에 참여.
- **승리 및 무승부 판별**: 승리 조건(가로, 세로, 대각선)을 실시간으로 판별하며, 무승부를 확인.
- **잘못된 입력 처리**: 플레이어가 잘못된 입력을 하면 안내 메시지를 제공.

---

## 게임 규칙

1. 플레이어는 차례대로 3x3 보드에 자신의 기호("X" 또는 "O")를 배치합니다.
2. 같은 기호를 가로, 세로, 또는 대각선으로 3개 연속으로 배치하면 승리합니다.
3. 모든 칸이 채워졌으나 승자가 없는 경우 무승부로 처리됩니다.

---

## 파일 구조

```
.
├── main.py          # 게임 실행 코드
└── README.md        # 프로젝트 설명 파일
```

---

## 실행 방법

1. Python 설치: Python 3.6 이상이 필요합니다.
2. 프로젝트 다운로드:
   ```bash
   git clone <repository-url>
   cd tic-tac-toe
   ```
3. 게임 실행:
   ```bash
   python main.py
   ```
4. 모드 선택:
   - "1"을 입력하면 플레이어 대 플레이어 모드로 시작합니다.
   - "2"를 입력하면 플레이어 대 AI 모드로 시작합니다.

---

## 코드 설명

### 주요 함수

1. **print_board(board)**:
   - 현재 보드를 출력합니다.

2. **check_winner(board, player)**:
   - 주어진 플레이어가 승리했는지 확인합니다.

3. **find_winning_move(board, player)**:
   - 주어진 플레이어가 이길 수 있는 위치를 찾습니다.

4. **get_valid_move(board, is_player, current_player)**:
   - 플레이어 또는 AI의 유효한 움직임을 반환합니다.

5. **play_game_with_mode(is_ai)**:
   - 게임의 주요 흐름을 제어합니다.

6. **main()**:
   - 게임 실행의 진입점으로 모드를 선택합니다.

---