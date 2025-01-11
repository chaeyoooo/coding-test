import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split()) # V는 정점, E는 간선
K = int(input()) # 시작번호
graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u,v,w = map(int, input().split()) #u에서 v로 가는 w가중치
    graph[u].append((v,w))

def dijkstra(K):
    q = []
    heapq.heappush(q,(0,K))
    distance[K] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V +1 ):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])