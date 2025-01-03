N = int(input())
A = set(map(int, input().split())) # list 시간 초과 일어나서 set으로 변경 ( set은 중복을 허용하지 않기에 시간복잡도가 O(1)이다. )
M = int(input())
B = list(map(int, input().split()))

for i in range(M): 
    if B[i] in A:
        print(1)
    else:
        print(0)