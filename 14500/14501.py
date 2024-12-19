n = int(input()) #총 일수
schedule = [tuple(map(int,input().split())) for _ in range(n)]  #상담 일정(T[i], P[i])

dp = [0] * (n+1)  #dp배열 초기화 (n+1)크기

# dp 역방향 계산
#dp배열: 각 날부터 퇴사일 까지 얻을 수 있는 최대 수익을 저장한다.
for i in range(n-1, -1, -1): #n-1일부터 0일까지 계산
    time, pay = schedule[i]
    if i + time <= n: #상담이 퇴사 전에 끝날경우
        dp[i] = max(dp[i + 1], pay + dp[i + time])  #상담을 안할때와 할 때 중 최대값
    else:   #상담이 퇴사 이후까지 걸리는 경우
        dp[i] = dp [i+1] #상담을 하지 않음

print(dp[0])  #첫째날부터 퇴사일까지 얻을 수 있는 최대 수익을 출력한다.