def solution(n, m, section):
#     entire = []
#     for i in range(1, n+1):
#         entire.append(i)
    
#     for j in range(len(section)):
    paintend = 0
    cnt = 0
    for i in range(len(section)):
        if section[i] > paintend:
            cnt += 1
            paintend = section[i] + m - 1
    return cnt
        