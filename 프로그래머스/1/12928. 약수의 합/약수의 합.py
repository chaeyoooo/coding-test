def solution(n): # n의 약수를 모두 더해서 출력해라 ! 예를 들어 
    stack = []
    k =  (n // 2 )+ 1
    for i in range(1, k):
        if n % i == 0:
            stack.append(i)
            
    stack.append(n)
    
    answer = sum(stack)
    return answer