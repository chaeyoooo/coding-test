# def solution(n, left, right):
#     array = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append(max(i,j) + 1)
#         array.append(row)
    
#     #2차원 배열 > 1차원
#     answer = sum(array , [])
#     return answer[left:right+1]

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row = i // n
        col = i % n
        answer.append(max(row, col) + 1)
    return answer