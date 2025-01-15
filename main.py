import random

# 게임 보드 출력 함수
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# 승리 조건 검사 함수
def check_winner(board, player):
    # 가로, 세로, 대각선 체크
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# 특정 플레이어가 이길 수 있는 위치 찾기
def find_winning_move(board, player):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board, player):
                    board[row][col] = " "
                    return row, col
                board[row][col] = " "
    return None

# 유효한 입력 받기 함수
def get_valid_move(board, is_player=True, current_player="O"):
    if not is_player:
        # AI의 턴
        # 1. AI가 이길 수 있는 위치 찾기
        winning_move = find_winning_move(board, current_player)
        if winning_move:
            return winning_move

        # 2. 플레이어의 승리를 막기 위한 위치 찾기
        opponent = "X" if current_player == "O" else "X"
        blocking_move = find_winning_move(board, opponent)
        if blocking_move:
            return blocking_move

        # 3. 랜덤으로 빈 칸 선택
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
        return random.choice(empty_cells)

    # 플레이어의 입력
    while True:
        try:
            row, col = map(int, input("행과 열을 입력하세요 (0, 1, 2): ").split())
        except ValueError:
            print("잘못된 입력입니다. 공백으로 구분된 두 개의 숫자를 입력하세요.")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            return row, col

        print("잘못된 이동입니다. 다시 시도하세요.")

# 게임 진행 함수
def play_game_with_mode(is_ai=False):
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0

    while True:
        print_board(board)
        print(f"{current_player}의 차례입니다.")

        # AI 또는 플레이어 입력 받기
        is_player_turn = current_player == "X" or not is_ai
        row, col = get_valid_move(board, is_player=is_player_turn, current_player=current_player)

        board[row][col] = current_player
        moves += 1

        # 승리 조건 확인
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} 승리!")
            break

        # 무승부 조건 확인
        if moves == 9:
            print_board(board)
            print("무승부입니다!")
            break

        # 플레이어 교체
        current_player = "O" if current_player == "X" else "X"

# 게임 실행
def main():
    print("틱택토에 오신 것을 환영합니다!")
    mode = input("모드를 선택하세요: '1' (플레이어 대 플레이어), '2' (플레이어 대 AI): ").strip()

    if mode == "1":
        play_game_with_mode(is_ai=False)
    elif mode == "2":
        play_game_with_mode(is_ai=True)
    else:
        print("잘못된 모드입니다. 게임을 다시 시작하세요.")

if __name__ == "__main__":
    main()
