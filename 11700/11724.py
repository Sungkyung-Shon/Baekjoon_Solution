import sys
from collections import defaultdict

def dfs(x):
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            dfs(node)

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = list([] for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
cnt = 0 #연결 요소 개수

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)