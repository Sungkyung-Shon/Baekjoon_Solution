import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()

def binary_search(target, arr):
    start = 0
    end = len(arr) - 1

    while start <= end: # start가 end를 넘지 않게
        mid = (start + end) // 2
        if arr[mid] == target:
            return arr.count(target)
        elif arr[mid] < target:
            start = mid +1
        else:
            end = mid - 1

for i in m_list:
    result = binary_search(i, n_list)
    if result == None:
        print(0, end =  " ")
    else:
        print(result, end = " ")

