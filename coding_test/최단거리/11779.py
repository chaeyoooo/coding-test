import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input()) #도시의 갯수
M = int(input()) # 버스의 갯수
graph = [[] for i in range( N +1 )]
distance = [INF] * (N+1)
previus = [-1] * (N+1)

for _ in range(M):
    start, end , cost = map(int, input().split())
    graph[start].append((end, cost)) # 그래프에 추가

def djistra(start):
    q =[]
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] # i[1]은 거리
            if cost < distance[i[0]]: #노드의 거리
                distance[i[0]] = cost
                previus[i[0]] = now
                heapq.heappush(q, (cost , i[0]))

start1, end1 = map(int, input().split())
djistra(start1)
print(distance[end1])
# print(previus)

path = []
while end1!= -1:  # 이전 노드가 없을 때까지 추적
    path.append(end1)
    end1 = previus[end1]
path.reverse()

# 경로 출력
print(len(path))  # 경로에 포함된 도시의 개수
print(' '.join(map(str, path)))  # 경로를 공백으로 구분하여 출력

