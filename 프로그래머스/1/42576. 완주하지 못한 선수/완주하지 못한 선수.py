from collections import Counter
def solution(participant, completion):
    a = list(Counter(participant)-Counter(completion))
    return "".join(a)
