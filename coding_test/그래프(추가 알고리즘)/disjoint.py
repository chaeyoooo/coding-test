#특정 원소가 속한 집합을 찾기
def find_parent(parent, x): #parent = [0, 1, 1, 1, 4, 5]
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

#두 원소가 속한 집합 합치기
def union_parent(parent, a , b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map (int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

#합칩합 연산
for i in range(e):
    a,b = map(int, input().split)
    union_parent(parent, a, b)

#각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent, i), end =" ")

print()

#부모 테이블 내용
for i  in range(1, v+1):
    print(parent[i] , end = " ")