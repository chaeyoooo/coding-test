#위상정렬
from collections import deque

#노드의 갯수와 간선의 갯수 입력 받기
v, e = map(int, input().split())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1) 
#각 노드에 연결 된 간선 정보를 담기위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

#방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

#위상 정렬 함수
def topology_sort():
    result = [] #리스트
    q = deque()

    #진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        #큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)

        #해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

        for i in result:
            print(i , end= " ")

topology_sort()
        
