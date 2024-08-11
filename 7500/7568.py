import sys

n = int(input())
weight = []
height = []
for i in range(n):
    w, h = map(int, sys.stdin.readline().split())
    weight.append(w)
    height.append(h)
for i in range(n):
    k = 1
    for j in range(n):
        if weight[i] < weight[j] and height[i] < height[j]:
            k += 1
    print(k, end =" ") 