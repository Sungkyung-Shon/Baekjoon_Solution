import sys

def dfs(idx):
    global visited
    visited[idx] = True #  방문한 노드는 true
    print(idx, end = ' ')
    for next in range(1, n+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited  #  q:큐
    while q:   #  큐의 요소가 남아있을때까지
        cur = q.popleft()   #  큐의 가장 첫번째 요소를 뺴낸다
        print(cur, end = ' ')
        for next in range(1, n+1):  #  cur에서 갈 수 있는 노드를을 q에 넣어준다
            if not visited[next] and graph[cur][next]:  # 방문 된적이 없는지 확인
                visited[next] = True  #  방문할 수 있다면 True로 바꿔준다.
                q.append(next)  #  큐의 맨 끝에 넣어준다.

#  입력 초기화
input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[False]*(n+1) for _ in range(n+1)]   #  (n+1)x(n+1) 2차원 배열
visited = [False] * (n+1)  #  1차원 배열

#  그래프 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

#  dfs
dfs(v)   #  v부터 dfs함수 시작 
print()   #  줄바꿈을 해주기 위해서

#  bfs
visited = [False] * (n+1)   #  방문을 안했다고 치고 다시 bfs를 해줘야 하니까 다 False로 바꿔준다.
q = [v]   #  큐에 v를 담아준다. (v부터 시작할거니까)
visited[v] = True   #  v를 재방문 하지 않도록
bfs()