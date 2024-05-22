n, k = map(int, input().split())

money = []
for _ in range(n):
    money.append(int(input()))

money.reverse()  
money_number = 0
for i in money:
    money_number += (k//i) 
    k %= i  
print(money_number)
