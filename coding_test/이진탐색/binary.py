def binary(array, target, start , end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary(array , target , start, mid -1)
    else :
        return binary(array , target , mid + 1, end)
    
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary(array, target, 0, n-1)
print(result)   