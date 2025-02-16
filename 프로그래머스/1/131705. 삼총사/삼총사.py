from itertools import combinations
def solution(number):
    cnt = 0
    result = combinations(number, 3) #이터레이터 객체
    for i in result:
        if sum(i) == 0:
            cnt += 1
    return cnt