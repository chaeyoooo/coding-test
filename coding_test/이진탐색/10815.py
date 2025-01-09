# N = int(input())
# have = list(map( int ,input().split()))

# M = int(input())
# check = list(map( int ,input().split()))

# for card in check:
#     if card in have:
#         print(1, end = ' ')

#     else:
#         print(0, end = ' ')

# 시간 초과 

def binary(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary(array , target, start, mid -1)
    else:
        return binary(array , target, mid + 1, end)

N = int(input())
have = sorted(list(map( int ,input().split()))) #이진 탐색 하려면 정렬

M = int(input())
check = list(map( int ,input().split()))

result = []
for card in check:
    result.append(binary(have, card, 0 , N-1))

print(*result) # 리스트 언패킹

    
