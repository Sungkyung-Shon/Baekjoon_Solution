n,m = map(int, input().split())
box = [i for i in range(1, n+1)]

for i in range(m):
    i, j = map(int, input().split())
    # temp = box[i-1:j]
    # temp.reverse()
    # box[i-1:j] = temp
    box[i-1:j] = box[i-1:j:-1]

for i in range(n):
    print(box[i], end=" ")

