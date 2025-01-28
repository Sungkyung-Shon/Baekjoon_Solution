# 입력 받기
bingo_board = [list(map(int, input().split())) for _ in range(5)]  # 빙고판 입력
calls = [int(x) for _ in range(5) for x in input().split()]  # 사회자가 부르는 숫자 입력

def count_bingo(board):
    count = 0

    # 가로 체크
    for row in board:
        if sum(row) == 0:  # 모두 0이면 빙고
            count += 1

    # 세로 체크
    for col in range(5):
        if sum(board[row][col] for row in range(5)) == 0:  # 각 열의 합이 0이면 빙고
            count += 1

    # 대각선 체크
    if sum(board[i][i] for i in range(5)) == 0:  # 좌상-우하 대각선
        count += 1
    if sum(board[i][4 - i] for i in range(5)) == 0:  # 우상-좌하 대각선
        count += 1

    return count

# 숫자를 하나씩 부르며 체크
def find_bingo_turn(board, calls):
    for turn, number in enumerate(calls, start=1):  # 몇 번째 숫자인지 추적
        # 빙고판에서 해당 숫자를 체크
        for i in range(5):
            for j in range(5):
                if board[i][j] == number:
                    board[i][j] = 0  # 숫자를 0으로 변경 (체크 표시)

        # 현재 빙고 줄 개수 계산
        if count_bingo(board) >= 3:  # 3줄 이상 빙고면
            return turn  # 현재 호출된 숫자의 순서 반환

# 결과 출력
print(find_bingo_turn(bingo_board, calls))
