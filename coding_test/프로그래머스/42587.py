#큐
from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    # deque([(0,2), (1,1), (2,3), (3,2)])  인덱스 , 우선순위로 저장
    
    count = 0
    
    #큐 앞으로 꺼내기
    while queue:
        current = queue.popleft()
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            count +=1
            if current[0] == location:
                return count