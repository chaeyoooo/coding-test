from collections import deque

K = int(input())    
for _ in range(K):
    N,M = map(int, input().split())
    importance = list(map(int, input().split()))

    queue = deque()
    for i in range(N):
        queue.append((importance[i], i))

    importance.sort(reverse=True)
    cnt = 0

    while queue:
        if queue[0][0] == importance[cnt]:
            cnt += 1
            if queue[0][1] == M:
                print(cnt)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())
    

