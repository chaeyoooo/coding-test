def solution(s):
    #문자열 > 정수로
    answer = []
    for i in s.split(): #리스트는 문자열에 공백있으면 안만들어짐 , list(s)가 아니라 s.split()사용
        answer.append(int(i))
    a,b = max(answer) , min(answer)
    return " ".join(map(str, [b,a])) #두개를 문자열로 만들고 싶으면 리스트로 묶어서
    #함수에서 