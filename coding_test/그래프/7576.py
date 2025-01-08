# from collections import deque

# M, N = map(int, input().split())    
# tomato = [input().split() for _ in range(N)]

# visited = [[-1] * M for _ in range(N)]  

# dy = [-1,1, 0, 0]   
# dx = [0, 0, -1, 1]  

# def bfs(start_y, start_x):
#     queue = deque([(start_y,start_x)])
#     visited[start_y][start_x] = 1
#     count = 1

#     while queue:
#         y,x = queue.popleft()

#         for i in range(4):
#             ny, nx = y + dy[i], x + dx[i]

#             if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == -1 and (tomato[ny][nx] == '0' or tomato[ny][nx] == '1'):
#                 visited[ny][nx] = visited[y][x] + 1
#                 queue.append((ny,nx))
#                 count += 1

#     return count

# whole = []
# for y in range(N):
#     for x in range(M):
#         if visited[y][x] == -1 and tomato[y][x] == '1' or tomato[y][x] == '0':
#             whole.append(bfs(y, x))


# print(len(whole))

from collections import deque

M, N = map(int, input().split())    
tomato = [input().split() for _ in range(N)]

dy = [-1, 1, 0, 0]   
dx = [0, 0, -1, 1]  

def bfs():
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and tomato[ny][nx] == '0':  # 익지 않은 토마토만 탐색
                tomato[ny][nx] = str(int(tomato[y][x]) + 1)  # 날짜를 증가시킴
                queue.append((ny, nx))

# 익은 토마토(1)의 위치를 큐에 추가
queue = deque()
for y in range(N):
    for x in range(M):
        if tomato[y][x] == '1':  # 익은 토마토
            queue.append((y, x))

bfs()  # BFS 실행

# 결과 계산
max_days = 0
for y in range(N):
    for x in range(M):
        if tomato[y][x] == '0':  # 익지 않은 토마토가 남아 있으면 -1 출력
            print(-1)
            exit()
        max_days = max(max_days, int(tomato[y][x]))

print(max_days - 1)  # 최대값에서 1을 뺀 결과 출력


# 아직 모르겠어서 추후에 보기 