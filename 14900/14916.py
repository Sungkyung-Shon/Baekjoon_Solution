import sys

n = int(sys.stdin.readline())
count = 0 #동전의 최소 개수
coins = [5,2]
for i in coins:
    count += (n//i)
    n %= i
print(count)
    
