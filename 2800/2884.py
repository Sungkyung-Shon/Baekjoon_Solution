hour, minute = map(int,input().split())

alarm = hour*60 + minute - 45
hour = alarm // 60
minute = alarm % 60
if hour==-1:
    hour=23

print(hour, minute)