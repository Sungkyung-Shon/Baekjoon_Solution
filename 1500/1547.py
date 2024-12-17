m = int(input())  # 교환 횟수
ball_position = 1 # 공위치는 처음에 1번 컵에 있음음
# ball_position은 공이 현재 있는 컵 번호

for _ in range(m):
    x, y = map(int, input().split()) 
    if ball_position == x:  # 공이 x번 컵에 있으면
        ball_position = y  # y컵으로 이동
    elif ball_position == y:  # 공이 y번에 있으면
        ball_position = x    # x컵으로 이동

print(ball_position) # 결과 출력력