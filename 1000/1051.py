n,m = map(int,input().split())
board = [list(map(int,input().strip())) for i in range(n)]

max_size = 1  # 최소 크기 (1x1)

for i in range(n):    # 행 인덱스
    for j in range(m):    #열 인덱스스
        # 가능한 정사각형 크기를 하나씩 키워가며 확인
        for k in range(1, min(n,m)):   # 가능한 변의 길이 k
            if i+k < n and j + k <m: #범위를 벗어나지 않아야 한다.
                # 아래로 : i+k <n 오른쪽으로 j+k <m
                if (board[i][j] == board[i][j+k] ==
                    board[i+k][j] == board[i+k][j+k]):
                    max_size = max(max_size, k+1)

print(max_size ** 2)
