from collections import deque

def dfs(graph, v, visited): # graph: 인접 리스트, v: 시작 노드, visited: 방문 여부
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited): # graph: 인접 리스트, start: 시작 노드, visited: 방문 여부
    queue = deque([start]) #큐(deque)사용하여  선입 선출 , 시작 노드를 넣어야함
    visited[start] = True
    while queue:
        v = queue.popleft() # 앞에 있는 요소 꺼내기
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N,M,V = map(int,input().split())
graph  = {i : [] for i in range(1,N+1)} #인접 리스트

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)

