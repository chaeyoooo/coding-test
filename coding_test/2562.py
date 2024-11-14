# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
    max_A = max(A)
    max_index = A.index(max_A)
print(max_A)
print(max_index+1)
# N = int(input())
# A = []
# for i in range(N):
#     A.append(int(input()))
#     # max_A = max(A)
#     # max_index = A.index(max_A)
#     if A[i-1]<A[i]:
#         max_A = A[i]
#         max_index = i

    
# print(max_A)
# print(max_index+1)


A = []
for _ in range(9):
    A.append(int(input()))  # 각 자연수를 입력받아 리스트 A에 추가

# 최댓값과 그 인덱스를 구합니다.
max_A = max(A)
max_index = A.index(max_A)

# 결과 출력
print(max_A)
print(max_index + 1)