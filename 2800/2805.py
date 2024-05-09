import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(tree)
result = 0 
while left <= right:
    num = 0
    mid = (left + right) // 2  
    for i in tree:
        if i > mid:
            num += i - mid
    if num < M:
        right = mid - 1
    else:
        result = mid
        left = mid + 1
print(result)  