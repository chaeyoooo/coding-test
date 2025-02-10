def solution(a, b):
    # a = [-1, 0 , 1]
    # b = [ 1, 0 , -1]
    # -1 + 0 + -1 = -2
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer