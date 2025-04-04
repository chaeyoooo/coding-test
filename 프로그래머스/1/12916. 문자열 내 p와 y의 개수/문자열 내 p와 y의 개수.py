def solution(s):
    s = s.upper()
    cnt1 = 0
    cnt2 = 0
    for i in s:
        if i == "P":
            cnt1 += 1
        elif i == "Y":
            cnt2 += 1
            
    if cnt1 == cnt2:
        answer = True #파이썬에서는 true x , True
    else:
        answer = False
    return answer