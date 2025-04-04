def solution(n):
    #00 연구소 > 한번에 k 칸 앞으로 점프(건전지 0) or 현재까지 온 거리 * 2 (순간이동)(건전지x)
    
    #이진수 구하고 1인거 count처리 해주기 !
    ones = bin(n)[2:].count('1')
    return ones
  