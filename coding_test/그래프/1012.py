from collections import deque

T = int(input())  

for i in range(T):
    M, N, K = map(int, input().split())  

    farm = [[0] * M for _ in range(N)] 
    visited = [[-1] * M for _ in range(N)]  

    for j in range(K):
        x, y = map(int, input().split()) 
        farm[y][x] = 1 

    dy = [-1, 1, 0, 0]  
    dx = [0, 0, -1, 1]

    def bfs(start_y, start_x):  
        queue = deque([(start_y, start_x)])
        visited[start_y][start_x] = 1
        count = 1

        while queue:
            y, x = queue.popleft()

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == -1 and farm[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
                    count += 1

        return count

    whole = [] 
    for y in range(N):
        for x in range(M):
            if visited[y][x] == -1 and farm[y][x] == 1:  
                whole.append(bfs(y, x)) 

    print(len(whole)) 
