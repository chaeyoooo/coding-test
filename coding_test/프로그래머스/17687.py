def solution(n, t, m, p):
    stack = []  # 변환된 숫자를 저장할 리스트
    answer = []  # 튜브가 말해야 하는 숫자 
    digits = "0123456789ABCDEF"  
    num = 0  # 숫자 0부터 시작

    while len(stack) < t * m:
        temp_num = num 

        if temp_num == 0:
            stack.append("0")
        else:
            temp_stack = []  
            while temp_num > 0:
                temp_stack.append(digits[temp_num % n]) 
                temp_num //= n  

            stack.extend(temp_stack[::-1]) 

        num += 1  

    for j in range(t):
        answer.append(stack[(p - 1) + j * m])  

    return ''.join(answer) 
