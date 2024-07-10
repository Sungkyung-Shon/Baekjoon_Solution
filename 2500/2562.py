numbers = []
for i in range(9):
    number = int(input())
    numbers.append(number)

print(max(numbers))
print(numbers.index(max(numbers))+1)

