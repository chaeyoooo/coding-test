def solution(n, m):
    answer = []
    a = 1 #최대 공약수 변수
    
    for i in range(1, min(n,m) + 1):
        if n % i == 0 and m % i == 0:
            a = i
            
    #최소 공배수
    b = (n * m) // a
    
    return [a,b]