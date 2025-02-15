def solution(arr):
    prev = arr[0]
    answer = []
    answer.append(prev)
    for i in arr[1:]:
        if prev != i:
            answer.append(i)
    
        prev = i
        
    return answer