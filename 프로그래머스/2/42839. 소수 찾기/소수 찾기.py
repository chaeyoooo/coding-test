from itertools import permutations
def solution(numbers):
    numbers = list(numbers)
    
    num_set = set()
    for i in range(1, len(numbers) + 1):
        perm = permutations(numbers,i)
        for p in perm:
            num = int("".join(p))  
            num_set.add(num)
    
    cnt = 0
    for num in num_set:
        if num <= 1:
            continue
            
        isPrime = True # 다 소수라고 일단 전제 깔기
        
        for i in range(2,int(num ** 0.5) + 1):
            if num % i == 0:
                isPrime = False # 2부터 루트 n까지 수에서 나누어 떨어지면 소수 아님
                break
        
        if isPrime:
            cnt +=1
            
    return cnt
        
        
        
    