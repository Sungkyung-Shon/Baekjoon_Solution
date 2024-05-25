n, m, k = map(int, input().split())   # n: 여학생 수, m: 남학생 수, k: 인턴쉽 학생 수
team = 0

while n>=2 and m>=1 and n+m >= k+3:  # 2명,1명 팀 만들수 있고, 인턴쉽도 보낼 수 있는 수일때
    n -= 2
    m -= 1
    team += 1
print(team)


