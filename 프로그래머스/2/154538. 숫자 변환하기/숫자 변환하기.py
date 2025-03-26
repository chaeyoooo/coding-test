# y에서 x로 가고자 함..!
#y에서 2로 나누면 
# y에서 3으로 나누면

from collections import deque
def solution(x, y, n):
    queue = deque()
    queue.append((x,0)) #현재 숫자 , 연산횟수
    visited = set()
    visited.add(x)
    
    while queue:
        current,num = queue.popleft() # 먼저 큐에서 제거
        
        if current == y:
            return num
        
        for next_num in (current + n , current * 2 , current *3):
            #방문처리
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num , num+1))
    return -1