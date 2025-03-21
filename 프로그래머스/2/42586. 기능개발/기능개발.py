
from collections import deque

def solution(progresses, speeds):
    que = deque()
    stack = []

    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            que.append((100 - progresses[i]) // speeds[i])
        else:
            que.append(((100 - progresses[i]) // speeds[i]) + 1)

    while que:
        x = que.popleft()
        result = 1
        while len(que) >= 1 and x >= que[0]:
            que.popleft()
            result += 1
        stack.append(result)
    return stack