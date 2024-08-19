import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int,sys.stdin.readline().split())
    n_list = list(map(int,sys.stdin.readline().split()))
    m_list = list(map(int, sys.stdin.readline().split()))

    n_list.sort()
    m_list.sort()

    count = 0 # 쌍의 개수 출력
    for i in n_list:
        start, end = 0, m-1
        while start <= end:
            mid = (start+end) // 2
            if m_list[mid] < i:
                start = mid + 1
            else:
                end = mid -1

        count += start  # 최종 start (m_list에서 i보다 작은 요소의 개수를 의미)
    print(count)
