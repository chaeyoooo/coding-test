N,M = map(int , input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

#방문 여부 초기화
visited = [[False] * M for _ in range(N)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#DFS 함수
def dfs(graph , i , j , visited):
    visited[i][j] = True #현재위치 방문 표시

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]

        if 0 <= ni < N and 0 <= nj < M:
            if not visited[ni][nj] and graph[ni][nj] == 0:
                dfs(graph,ni,nj,visited) # 위치 갱신 하면서 재귀함수 호출

count = 0

for i in range(N):
    for j in range(M):
         if not visited[i][j] and graph[i][j] == 0:
             dfs(graph , i , j , visited)
             count+=1

print(count)


        