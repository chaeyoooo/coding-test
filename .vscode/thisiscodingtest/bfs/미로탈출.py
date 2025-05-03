from collections import deque
queue = deque()

N,M = map(int , input().split())

graph = []
for i in  range(N):
    graph.append(list(map(int,input().split())))

queue.append((0,0)) #초기위치 설정

dx = [0,1,0,-1] #남북
dy = [1,0,-1,0] #동서

count = 0

while queue: #큐가 빌때 까지
        x,y = queue.popleft()

        for i in range(4):
             nx = x + dx[i]
             ny = y + dy[i]

             if 0 <= nx < N and 0<= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

print(graph[N-1][M-1])

