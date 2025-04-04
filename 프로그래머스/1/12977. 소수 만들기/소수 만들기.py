from itertools import combinations
import math
def solution(nums):
    #조합
    result = []
    answer = []
    for i in combinations(nums, 3):
        result.append(sum(i))
        
    for j in range(len(result)):
        prime  = True
        for k in range(2, int(math.sqrt(result[j])) +1):
            if result[j] % k == 0: # 소수 아니면
                prime = False
                break
        if prime:
            answer.append(result[j])
    return len(answer)
        
        