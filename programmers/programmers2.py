<<<<<<< HEAD
# 입국심사
def solution(n, times):
    left, right = 1, min(times) * n  
    while left <= right:
        mid = (left + right) // 2
        people = 0 
        for time in times:
            people += mid // time
        if people < n:
            left = mid + 1
        else:
            result = mid
            right = mid - 1
    return result
=======
def solution(n, times):
    left, right = 1, min(times) * n  
    while left <= right:
        mid = (left + right) // 2
        people = 0 
        for time in times:
            people += mid // time
        if people < n:
            left = mid + 1
        else:
            result = mid
            right = mid - 1
    return result
>>>>>>> 01ee2f10e010aaca813e9967a260041a6a406e9a
