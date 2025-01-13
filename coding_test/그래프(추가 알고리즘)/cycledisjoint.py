#특정 원소가 속한 집합을 찾기
def find_parent(parent, x): #parent = [0, 1, 1, 1, 4, 5]
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합 합치기
def union_parent(parent, a , b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 갯수와 간선의 갯수 입력 받기
v, e = map (int, input().split())
parent = [0] * (v+1)

#부모 테이블에서 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a,b = map(int, input().split())
    if find_parent(parent, a ) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)