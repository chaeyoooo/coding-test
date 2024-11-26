# n = int(input())
# rope = [int(input()) for _ in range(n)]
# rope.sort(reverse=True)
# if n == 1:
#     print(rope[0])
# else:
#     print(max(rope[i]) * n)

    # 처음에 생각을 했을 때 루프의 갯수 * 루프의 최소값을 해야한다고 생각했는데
    # 그게 아니라 만약 예시를 들면 로프를 내림차순 정렬: [15, 10, 5]

# 계산:
# 1개 사용: 
# 15×1 = 15
# 15×1=15
# 2개 사용: 
# 10 × 2 = 20
# 10×2=20 ⬅ 최대값
# 3개 사용: 
# 5 × 3 = 15
# 5×3=15

#이런식으로 각 단계별로 최댓값을 구해야함
#오름차순으로 정렬한다음에 제일 큰 값 * 1을 해주면 됨
#그 다음으로 큰 값 * 2를 해주면 됨
#이런식으로 계속 반복하면 됨
#그렇기 때문에 정렬을 해주는 것이 중요함
#그리고 그 중에서 최댓값을 구해주면 됨


n = int(input())
rope = [int(input()) for i in range(n)]
rope.sort() #작은 것 부터 정렬
max_weight = 0
for i in range(n):
    max_weight = max(max_weight, rope[i] * (n-i)) #그전에 저장한 max_weight와 비교해서 더 큰 값을 저장

print(max_weight)

