def solution(str1, str2):
    # 대문자로 변환
    str1 = str1.upper()
    str2 = str2.upper()

    # 다중집합 
    A = []
    for i in range(len(str1)-1):
        string1 = str1[i:i+2]
        if string1.isalpha(): 
            A.append(string1)

    B = []
    for j in range(len(str2)-1):
        string2 = str2[j:j+2] 
        if string2.isalpha():
            B.append(string2) 
            
    print(A) #['FR', 'RA', 'AN', 'NC', 'CE']
    print(B) #['FR', 'RE', 'EN', 'NC', 'CH']


    # 합집합 
    a_temp = A.copy()
    a_result = A.copy()  # 합집합 리스트

    for i in B:
        if i not in a_temp:  
            a_result.append(i)
        else:  # 공통으로 존재하면 하나 제거 (중복 방지)
            a_temp.remove(i)

    # 교집합
    result1 = [] 
    A_copy = A.copy() 

    for i in B:
        if i in A_copy:
            A_copy.remove(i)  #중복된거 제거
            result1.append(i)  

    print("교집합:", result1)
    print("합집합:", a_result)

    #유사도 계산
    if len(a_result) == 0:
        answer = 65536  
    else:
        answer = int((len(result1) / len(a_result)) * 65536)  

    return answer
