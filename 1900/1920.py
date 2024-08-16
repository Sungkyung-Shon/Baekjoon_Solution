import sys

def binary_search(target, arr):
    start = 0
    end = len(arr) - 1
    
    while start <= end:  #start가 end를 넘지 않게
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1   #target이 있다면 1 리턴
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid -1
    return 0   #target이 없다면 0 리턴

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()

for i in m_list:
    result = binary_search(i, n_list)
    print(result)