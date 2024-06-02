import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50



def dfs(y, x):
    global visited
    visited[y][x] = True



#  입력 초기화
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph=[[False]*MAX for _ in range(MAX)]
    visited=[[False]*MAX for_ in range(MAX)]

#  그래프 정보 입력
    for _ in range(k):
        x, y = map(int,input().split())
        graph[y+1][x+1] = True
    
#  방문하지 않은 지점부터 dfs돌기
answer = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] and not visited[i][j]:
            dfs(i,j)
            answer +=1
print(answer)