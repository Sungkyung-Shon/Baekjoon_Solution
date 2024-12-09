n = int(input()) #입력값으로 분해합을 받는다.
for i in range(1, n+1):
    num= sum(map(int, str(i)))  # i의 각 자릿수를 더한다
    num_sum = i + num # 분해합 = 생성자 + 각 자리수의 합
    if num_sum == n: # num_sum이 분해합과 같으면
        print(i)
        break
    if i == n: # 생성자i와 입력값이 같다는 것은 생성자가 없다는 뜻이므로 0을 출력해준다.
        print(0) 

