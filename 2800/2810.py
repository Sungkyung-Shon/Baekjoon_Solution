n = int(input())
seats = input()

couple = seats.count("LL")

if couple <= 1:
    print(n)
else:
    print(n+1-couple)