def solution(n):
    stack = []
    result = 0
    while n > 0:
        j = n % 3 
        n = n // 3
        stack.append(j) # 리스트
    

    stack = stack[::-1]
    
    for i in range (len(stack)):
        result += stack[i] * (3 **i )
    
    return result