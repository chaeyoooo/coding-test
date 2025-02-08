def is_prime_number(x):
    if x < 2:  # 0과 1은 소수 x
        return False
    for i in range(2, int(x ** 0.5) + 1): 
        if x % i == 0:
            return False  
    return True  # 반복문 끝날때 ?

def solution(n, k):
    stack = []
    
    # n을 k진수로 변환
    while n > 0:
        j = n % k #j 나머지
        n = n // k
        stack.append(j)

    result = ''.join(map(str, stack[::-1])) 
    
    newresult = result.split("0")  # 0을 기준으로 나누기

    # 빈 문자열 제거 + 숫자로 변환
    filter = []
    for x in newresult:
        if x != "":  
            filter.append(int(x)) 

    # 소수 개수 세기
    primecnt = 0
    for num in filter:
        if is_prime_number(num):  
            primecnt += 1

    return primecnt  
