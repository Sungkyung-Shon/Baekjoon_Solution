import sys

n, k = map(int, sys.stdin.readline().split())

cable = []

for i in range(n):
    cable.append(int(input()))

left, right = 1, max(cable)
while left <= right:
    x =0
    mid = (left+right) // 2
    for j in cable:
        if j >= mid:
            x += j//mid
    if x < k:
        right = mid-1
    else:
        result = mid
        left = mid+1
print(result)