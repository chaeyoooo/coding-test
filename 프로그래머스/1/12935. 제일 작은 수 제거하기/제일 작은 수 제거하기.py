def solution(arr):
    #제일 작은 수 return 하는 것
    k = min(arr)
    arr.remove(k)
    
    if not arr:
        return [-1]
    else:
        return arr