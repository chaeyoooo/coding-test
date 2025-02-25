def solution(dartResult):
    #점수 , Single , Double , Triple (1제곱 . 2제곱 . 3제곱)
    #옵션 스타상(*) 해당 점수와 전 점수의 2배 / 처음은 해당만, 아차상(#) 해당점수 마이너스
    # 스타상의 효과는 다른 스타상의 효과와 중첩 ㄱㄴ 중첩된 스타상 점수 4배
    # 스타상 아차상 효과와 중첩될 수 0 , 중첩된 아차상 점수는 -2배
    #문자열 나누기 만약 숫자 하고 문자가 나오니까 ..
    temp = ""
    result = []
    for i in dartResult:
        if i.isdigit():
            temp += i
        elif i in ('S', 'D', 'T'):
            if i == 'S':
                result.append(int(temp))
            elif i =="D":
                result.append(int(temp)**2)
            else:
                result.append(int(temp)**3)
            temp =""
        elif i in ("*", "#"):
            if i == "*":
                result[-1] *= 2
                if len(result) > 1:
                    result[-2] *= 2
            elif i =="#":
                result[-1] *= -1           
    return sum(result)