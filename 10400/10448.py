triangle = []
for i in range(1, 46):    # k<1000 이므로
    triangle.append(i*(i+1)//2)  # triangle의 리스트를 만들어준 후 triangle(Tn)을 정의해준다.

eureka =[0] * 1001 #정답 리스트를 0으로 초기화.

for i in triangle:
    for j in triangle:
        for k in triangle:
            num = i + j + k
            if num <= 1000:
                eureka[num] =1 # 세수 i+ j+ k의 합이 1000보다 작으면 1


n = int(input())
for i in range(n):  # 입력받기
    num = int(input())
    print(eureka[num])

