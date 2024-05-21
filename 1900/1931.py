import sys

n= int(input())
meeting = []

for _ in range(n):
    start, end = map(int,input().split())
    meeting.append((start,end))
    
meeting = sorted(meeting, key = lambda x: (x[1], x[0]))

end_time = meeting[0][1]
number_meeting = 1  
for i in range(1,n):   
    if end_time <= meeting[i][0]:  
        end_time = meeting[i][1]
        number_meeting +=1
print(number_meeting)


