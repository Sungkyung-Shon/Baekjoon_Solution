import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
cable = deque()

for i in range(1, n+1):
    cable.append(int(input()))

left, right = 1, max(cable)  #  1 <= 랜선 최대의 길이 <= max(cable)
while left <= right:
    x = 0 # 랜선의 개수
    mid = (left + right) // 2
    for j in cable:
        if j >= mid:
            x += j//mid  #  몫 = 랜선의 개수
    if x < k:
        right = mid-1
    else:
        result = mid
        left = mid+1
print(result)

