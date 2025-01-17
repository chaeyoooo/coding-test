# N,M = map(int, input().split())
# number = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     for j in range(N):
#         if number[i] != number[j]:
#             cnt += 1

# print(cnt)
N, M = map(int, input().split())
number = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i + 1, N):  # j는 항상 i보다 큰 값
        if number[i] != number[j]:  # 무게가 다를 때만
            cnt += 1

print(cnt)
