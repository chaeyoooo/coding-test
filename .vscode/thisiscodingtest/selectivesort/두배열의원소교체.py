N, K = map(int, input().split())
A = list(map(int, input()).split())
B = list(map(int, input()).split())

# for i in range(len(A)):
#     min_index = A[i]
#     if A[i+1] < min_index:
#         min_index = A[i+1]
#     else:
#         A[i]


A.sort(reverse = False)
B.sort(reverse = True) #큰값 부터

count = 0

for i in range(K):
    if A[i] < B[i]:
       A[i] , B[i] = B[i] , A[i]

for j in A:
    count += int(j)

print(count)