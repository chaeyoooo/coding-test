def solution(n):
    # 재귀식 시간 소요 큼
    a , b = 1,1
    if n == 1 or n == 2:
        return 1
    for i in range(1 , n):
        a , b = b , a+b
    return a % 1234567