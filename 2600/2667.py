import sys

#  bfs: 시작 위치 받아서, 해당 위치에 연결된 1의 개수 리턴
def bfs(start_i, start_j):  # start i, start j
    q = []   #  큐 생성

    q.append((start_i, start_j))  # 큐 초기 데이터 삽입
    visited[start_i][start_j] = 1
    cnt = 1

    while q:
        current_i, current_j = q.pop(0) 
        for direction_i, direction_j in ((-1,0),(1,0),(0,-1),(0,1)):  #  상하좌우
            next_i, next_j = current_i+direction_i, current_j+direction_j   
            #  4방향, 범위내, 미방문, 1이면 q삽입
            if 0<=next_i<n and 0<next_j<n and visited[next_i][next_j]==0 and graph[next_i][next_j]==1:
                q.append((next_i,next_j))
                visited[next_i][next_j]=1
                cnt+=1
    return cnt

input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
#graph = [list(int(input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        #  방문하지 않았던 아파트 발견시 bfs
        if graph[i][j]==1 and visited[i][j]==0:
            ans.append(bfs(i,j))

ans.sort()
print(len(ans), *ans, sep='\n')