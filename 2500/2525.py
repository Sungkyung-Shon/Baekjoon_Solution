hour, minute = map(int,input().split())
cooking_time = int(input())

if minute + cooking_time < 60:
    print(hour, minute+cooking_time)
else:
    if minute+cooking_time-60 != 60:
        if hour + 1 == 24:
            print(0, minute+cooking_time-60)
        else:
            print(hour+1, minute+cooking_time-60)
    else:
        if hour + 1 == 24:
            print(0, minute+cooking_time-60)
        else:
            print(print(hour+1, 0))