def solution(s):
    s = s.split(" ")
    answer = ""
    for i in s:
        if i:
            if i[0].isalpha(): #자료형인지 확인 방법 : isalpha()!!
                answer += i[0].upper()
                answer += i[1:].lower()
            else:
                answer += i[0]
                answer += i[1:].lower()
        answer += " " 
    return answer[:-1]