INF = int(1e9)

v,e = map(int, input().split()) #v는 노드 , e는 간선
graph = [[INF] * ( v + 1 ) for _ in range(v+1)]

#자기 자신에서 자기 자신으로 가는 비용 > 0 , 이중 for 문으로 확인 하면 에러 발생 ..!
for i in range(1, v+1):
    graph[i][i] == 0

#각 간선에 대한 정보 받아서 그값으로 초괴화
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b],c)

#각 점화식에 따라 알고리즘 수행
for k in range(1,v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])

#여기서 중요한점 ( 사이클 , 다시 돌아오는 경우를 구해야됨! )
cycle = INF
for i in range(1 , v+1):
    cycle  = min( cycle , graph[i][i])

if cycle == INF:
    print("-1")
else:
    print(cycle)
