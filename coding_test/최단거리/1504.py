import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N,E = map(int, input().split())
graph = [[] for i in range(N+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) #양방향 그프
    graph[b].append((a,c)) #양방향 그래프

def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q ,(0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q , ( cost ,i[0]))
    return distance

u,v = map(int, input().split())

d1 = dijkstra(1)
du = dijkstra(u)
dv = dijkstra(v)

path1 = d1[u] + du[v] + dv[N]
path2 = d1[v] + dv[u] + du[N]

result = min(path1, path2)
if result >= INF:
    print(-1)
else:
    print(result)

