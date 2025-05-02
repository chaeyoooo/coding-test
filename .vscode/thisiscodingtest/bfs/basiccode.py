from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    queue = deque([start])   
    visited[start] = True    

    while queue:              # 큐가 빌 때까지 반복
        v = queue.popleft()   # 큐에서 하나 꺼냄
        print(v, end=' ')     # 방문한 노드 출력

        for i in graph[v]:    # 현재 노드와 연결된 노드들 확인
            if not visited[i]: # 방문하지 않은 노드라면
                queue.append(i)  # 큐에 넣고
                visited[i] = True # 방문 처리

# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
    [],          # 0번 노드는 사용하지 않음
    [2, 3, 8],   # 1번 노드와 연결된 노드들
    [1, 7],      # 2번 노드와 연결된 노드들
    [1, 4, 5],   # 3번 노드와 연결된 노드들
    [3, 5],      # 4번 노드와 연결된 노드들
    [3, 4],      # 5번 노드와 연결된 노드들
    [7],         # 6번 노드와 연결된 노드들
    [2, 6, 8],   # 7번 노드와 연결된 노드들
    [1, 7]       # 8번 노드와 연결된 노드들
]

# 각 노드의 방문 여부를 False로 초기화
visited = [False] * 9

# BFS 함수 호출 (1번 노드부터 시작)
bfs(graph, 1, visited)
