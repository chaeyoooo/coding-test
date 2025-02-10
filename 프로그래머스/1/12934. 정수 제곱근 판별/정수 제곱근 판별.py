def solution(n):
    answer = -1
    for i in range(1, int(n ** 0.5) + 2):
        if n == int(i) * int(i):
            if i > 0:
                answer = (i+1) * (i+1)
            break
    return answer