def solution(x):
    k = sum(list(map(int, str(x))))
    if x % k == 0:
        answer = True
    else:
        answer = False
    return answer