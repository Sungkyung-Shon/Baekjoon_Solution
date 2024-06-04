# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# MAX = 50

# dirX = [1,-1,0,0]
# dirY = [0,0,1,-1]  

# def dfs(x,y):
#     global visited
#     visited[x][y] = True
#     for dirIdx in range(4):
#         newX = x + dirX[dirIdx]
#         newY = y + dirY[dirIdx]
#         if graph[newX][newY] and not visited[newX][newY]:
#             dfs(newX, newY)

# # 입력 초기화
# t = int(input())  # 테스트 케이스 개수
# for _ in range(t):
#     m, n, k = map(int, input().split())  # 가로, 세로, 위치 개수
#     graph = [[False] * MAX for _ in range(MAX)]
#     visited = [[False] * MAX for _ in range(MAX)]

#     #  그래프 정보 입력
#     for _ in range(k):
#         x, y = map(int, input().split())
#         graph[x+1][y+1] = True  # 0,0 베이스

#     #  방문하지 않은 지점부터 dfs돌기
#     answer = 0 
#     for i in range(1, m+1):  # 가로
#         for j in range(1, n+1):   # 세로
#             if graph[i][j] and not visited[i][j]:
#                 dfs(i,j)
#                 answer +=1
#     print(answer)



import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50

dirX = [1,-1,0,0]
dirY = [0,0,1,-1]  

def dfs(x,y):
    graph[x][y] = False
    for dirIdx in range(4):
        newX = x + dirX[dirIdx]
        newY = y + dirY[dirIdx]
        if graph[newX][newY]:
            dfs(newX, newY)

# 입력 초기화
t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    m, n, k = map(int, input().split())  # 가로, 세로, 위치 개수
    graph = [[False] * MAX for _ in range(MAX)]

    #  그래프 정보 입력
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x+1][y+1] = True  # 0,0 베이스

    #  방문하지 않은 지점부터 dfs돌기
    answer = 0 
    for i in range(1, m+1):  # 가로
        for j in range(1, n+1):   # 세로
            if graph[i][j]:
                dfs(i,j)
                answer +=1
    print(answer)
