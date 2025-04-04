def solution(n): #n이 118372이면 873211
    n = list(map(int, str(n))) #문자열 > 리스트
    n.sort(reverse=True)
    k = ''.join(map(str, n)) #리스트 > 문자열
    return int(k)

