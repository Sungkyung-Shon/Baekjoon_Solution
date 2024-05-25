n = input()
n = sorted(n, reverse = True)   # 30의 배수가 되는 가장 큰 값은 이 수를 내림차순으로 정렬

num_sum = 0
if "0" not in n:  # n 에 0이 없으면
    print(-1)  #  -1 출력
else:
    for i in n:
        num_sum += int(i)  #  각 자리 수의 합
    if num_sum % 3 != 0:  # 각 자리 수의 합이 3의 배수가 아니면 
        print(-1)   # -1 출력
    else:
        print("".join(n))

