# n,g = map(int,input().split())
# coins = []
# for _ in range(n):
#     coins.append(int(input()))
# cnt = 0
# for i in range(n-1,-1,-1):
#     if g == 0:
#         break
#     if coins[i] <= g:
#         cnt += g // coins[i]
#         g %= coins[i]
# print(cnt)

# n,g = map(int,input().split())
# coins = []
# coin = int(input())
# cnt = 0
# for a in range(n):
#     coins.append(coin)

# if g < coins[i]:
#     cnt = g // coins[i]
#     g %= coins[i]
#     print(cnt)

# n, g = map(int, input().split())  # n: 동전 종류의 개수, g: 목표 금액
# coins = []                        # 동전 리스트
# cnt = 0                           # 필요한 동전 개수 초기화

# # 동전 값 입력받기
# for _ in range(n):
#     coin = int(input())
#     coins.append(coin)

# # 동전을 작은 값부터 사용하도록 정렬
# coins.sort()  # 오름차순 정렬

# # 목표 금액 만들기 (작은 동전부터 사용)
# for coin in coins:
#     if g < coin:  # 목표 금액이 현재 동전보다 작으면 계산 종료
#         break
#     cnt += g // coin  # 필요한 동전 개수 추가
#     g %= coin         # 남은 금액 계산

# # 결과 출력
# if g == 0:
#     print(cnt)  # 최소 동전 개수 출력
# else:
#     print(-1)   # 목표 금액을 만들 수 없는 경우


n,k = map(int,input().split())
coins =[]
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True) # 큰 값 부터 정렬 하겠다 !
cnt = 0
for coin in coins:
    if k >= coin:
        cnt += k // coin
        k = k % coin

print(cnt)