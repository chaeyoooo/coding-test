from collections import deque


N, M = map(int, input().split())
maze = [input().strip() for _ in range(N)]  


visited = [[-1] * M for _ in range(N)]

# 방향 이동 설정 (위, 아래, 왼쪽, 오른쪽)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS 함수 정의
def bfs():
    queue = deque([(0, 0)])  # 시작점 (0, 0)
    visited[0][0] = 1  # 시작점은 이동 횟수 1로 초기화

    while queue:
        y, x = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 미로 범위 안에 있어야 하고, 길(1), 이동할 수 있어야하니까 방문 하지 않은 칸이어야함!
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == '1' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1  
                queue.append((ny, nx))  


bfs()


print(visited[N-1][M-1])
