def solution(s):
    # 항상 먼저 문제 풀 때 s가 문자열인지 , 리스트인지 확인하기 ! 
    # 이후 문자열이면 인덱스를 다루어야하기 때문에 리스트로 바꾸기 !
    # 먼저 공백 문자로 나누고 
    # 짝수 번째를 대문자 , 홀수 번째를 소문자로 변경하기
    result = s.split(" ") # 나누고
    
    answer = list(result)
    for i in range(len(answer)):
        listi = list(answer[i])
        for k in range(len(listi)):
            if k % 2 == 0:
                listi[k] = listi[k].upper()
            else:
                listi[k] = listi[k].lower()    
            
        answer[i] = "".join(listi)
        
    return " ".join(answer)
        
        
    