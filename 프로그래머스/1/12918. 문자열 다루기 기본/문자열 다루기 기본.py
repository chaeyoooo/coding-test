def solution(s):
    a = len(s)
    if a == 4 or a == 6:
        return s.isdigit() #isdigit은 4 or 6이 아니면 none반환
    else:
        return False