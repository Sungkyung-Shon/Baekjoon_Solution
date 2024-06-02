x = int(input())
n = int(input())
total = 0
for i in range(n):
    cost, num = map(int, input().split())
    total = total + cost*num

if total == x:
    print("Yes")
print("No")



