
def bfs(start, end):
    #큐, visited[], 필요 변수 생성
    q = []
    visited = [0]*200001

    #초기데이터 삽입, visited[]초기화
    q.append(start)
    visited[start] = 1

    while q:
        current = q.pop(0)
        if current == end:
            return visited[end]-1
        #3방향, 범위내(0~200000), 미방문
        for next in (current-1, current+1, current*2):
            if 0<=next<=200000 and visited[next]==0:
                q.append(next)
                visited[next] = visited[current]+1
    
    # 이곳에 도달할 일 없지만
    return -1

n, k = map(int, input().split())
ans = bfs(n, k)
print(ans)