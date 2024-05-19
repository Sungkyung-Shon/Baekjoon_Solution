n = int(input())
people = list(map(int, input().split()))

people.sort()   #  1 2 3 3 4
time = 0
result = 0
for i in range(n):
    time += people[i]
    result += time
print(result)