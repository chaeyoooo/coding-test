def solution(elements):
    n = len(elements)
    circle = elements * 2
    answer = set()
    
    for i in range(1, n+1):
        for start in range(n):
            a = sum(circle[start: start + i])
            answer.add(a)
    return len(answer)