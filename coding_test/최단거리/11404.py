INF = int(1e9)

n = int(input()) # 노드의 갯수
m = int(input()) # 정점의 갯수

graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화 
for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보 받아 그 값으로 초기화

for _ in range(m):
    #a에서 b 로 가는 비용 c라고 설정
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range( 1, n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])


#수행된 알고고리즘 출력
for a in range(1, n+1):
    for b in range ( 1, n+1):
        if graph[a][b] == INF:
            print("0" , end = " ")
        else:
            print(graph[a][b], end= " ")
    print("")