# import sys
# from collections import deque

# people = deque()

# n, k = map(int, sys.stdin.readline().split())

# for i in range(1, n+1):
#     people.append(i)

# result = []
# i = 0
# while len(people) > 0:
#     for j in range(1, k):
#         people.append(people.popleft())
#     result.append(people.popleft)

# print(str(result).replace('[', '<').replace(']', '>'))


import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
people = deque

for i in range(1, n+1):
    people.append()

result = []
for i in range(1, n+1):
    for j in range(1,k):
        people.append(people.popleft())
    result.append(people.popleft)

print(str(result).replace('[', '<').replace(']', '>'))
