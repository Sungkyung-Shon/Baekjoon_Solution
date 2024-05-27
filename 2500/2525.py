hour, minute = map(int,input().split())
cooking_time = int(input())

hour += cooking_time//60
minute += cooking_time%60

if minute >=60:
    minute-=60
    hour+=1

if hour>=24:
    hour-=24

print(hour, minute)