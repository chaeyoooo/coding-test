#1647 
import sys
input = sys.stdin.readline
#find_parent
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#union_parent
def union_parent(parent, a , b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] =a
    else:
        parent[a] = b

#이제 입력
n,m = map(int, input().split())
parent = list(range(n+1))
edges = []
result = 0

#간선 정보 입력받기
for _ in range(m):
    a,b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort() # 비용 순으로 정렬
last = 0 # 가장 비용이 큰 간선

for edge in edges:
    cost , a , b = edge #edge의 튜플 명확히 하기 위해서 예를 들어 (3,1,2면 각각 변수 이름 할당 해주기 )
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)
