from itertools import combinations
def solution(numbers):
    answer = []
    result = list(combinations(numbers,2))
    for i in result:
        answer.append(sum(i))
        
    return sorted(set(answer))