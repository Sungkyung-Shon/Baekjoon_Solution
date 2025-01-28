import sys
input = sys.stdin.readline

a, b = map(int, input().split())
total = 9*17 # 카드 18장 중에 뽑을 수 있는 전체 카드 조합
answer = 0

if a == b: # 땡의 경우
    answer = total - (10-a)
else:
    mypoint = (a+b) % 10
    for i in range(1,11):
        for j in range(i+1, 11):
            if mypoint > (i+j)%10:
                if i ==a and j ==b:
                    continue
                elif i ==a or j == a or i ==b or j == b:
                    answer +=2
                else:
                    answer +=4

print("%.3f" %(answer/total))