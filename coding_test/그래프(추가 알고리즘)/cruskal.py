#부모 찾기
def find_parent(parent, x):
    if parent[x]!= x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
#두원소가 속한 집합 찾기
def union_parent(parent, a , b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
#노드의 갯수와 간선의 갯수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

#부모 테이블에서 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#모든 간선에 대한 정보 입력받기
for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost, a , b))

edges.sort()

for edge in edges:
    cost, a, b =edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)