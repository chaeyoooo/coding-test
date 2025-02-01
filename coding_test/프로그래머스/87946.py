from itertools import permutations

def solution(k, dungeons):
    all = list(permutations(dungeons)) #전체 경우의 수 리스트 출력, all을 사용하지 않는 문제 존재
    maxcount = 0
    
    for each in all:
        currentk = k
        count = 0
    
    #탐헌 가능한지 확인(최소 필요도 <= 현재 필요도) , 현재 필요도 - 소모 필요도
        line = len(dungeons)
        for i in range(line):
            if currentk - each[i][0] >=0:
                count +=1
                currentk = currentk - each[i][1]
            else:
                break
        
        maxcount = max(maxcount, count)
    
    return maxcount

