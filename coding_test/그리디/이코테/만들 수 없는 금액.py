N = int(input())
coin = list(map(int, input().split()))
coin.sort()

# for i in coin:
#     for j in coin:
#         a = i+j

# #a랑 i랑 j중에서 선택되지 않은 가장 최솟값을 구하면 됨!

target = 1 #만들 수 있는 금액의 최솟값
for i in coin:
    if i > target:
        break
    target += i

print(target)