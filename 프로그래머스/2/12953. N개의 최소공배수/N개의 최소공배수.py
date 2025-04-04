def solution(arr):
    answer = 1
    for i in range(len(arr)):
        answer *= arr[i]
        
    for j in range(max(arr) , answer +1):
        if all(j % num == 0 for num in arr):
            return j 

        