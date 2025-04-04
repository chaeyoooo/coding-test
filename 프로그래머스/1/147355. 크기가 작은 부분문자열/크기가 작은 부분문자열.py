def solution(t, p):
    plen = len(p)
    cnt = 0
    for i in range(len(t)):
        k = t[i:i+plen]
        if len(k) == plen:
            if k <= p:
                cnt += 1
    return cnt