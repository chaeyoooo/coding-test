def solution(n):
    count = 0
    # 1부터 n까지를 연속 수열의 시작점으로 고려
    for i in range(1, n+1):
        total = 0
        # 시작점 i부터 n까지 연속된 수들을 더하기
        for j in range(i, n+1):
            total += j
            if total == n:
                count +=1
                break
            elif total > n:
                break
    return count