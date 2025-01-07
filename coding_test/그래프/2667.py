from collections import deque

# 입력 받기
N = int(input())
apart = [input().strip() for _ in range(N)]

# 방문 여부 기록 (-1: 방문하지 않음, 1 이상: 방문 순서 또는 집 수)
visited = [[-1] * N for _ in range(N)]

# 이동 방향 (위, 아래, 왼쪽, 오른쪽)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(start_y, start_x):
    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = 1
    count = 1  # 현재 단지의 집 개수

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 지도 범위 내, 방문하지 않았으며, 집(1)인 경우
            if 0 <= ny < N and 0 <= nx < N and apart[ny][nx] == '1' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))
                count += 1  # 집 개수 증가

    return count

# 지도 전체 탐색
complex_sizes = []
for y in range(N):
    for x in range(N):
        if apart[y][x] == '1' and visited[y][x] == -1:
            # 새 단지를 발견하면 BFS 실행
            complex_sizes.append(bfs(y, x))

# 결과 출력
complex_sizes.sort()
print(len(complex_sizes))  # 총 단지 수
for size in complex_sizes:
    print(size)

