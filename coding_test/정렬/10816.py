N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
numbers2 = list(map(int, input().split()))

for i in range(M):
    if numbers2[i] in numbers:
        print(numbers.count(numbers2[i]), end = ' ')
    else:
        print(0, end = ' ')


#시간 초과 ... 
# 이진탐색을 이용해야 한다...