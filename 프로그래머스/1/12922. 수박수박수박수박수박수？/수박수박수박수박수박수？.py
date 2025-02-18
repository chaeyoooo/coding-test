# def solution(n):
#     answer = []
#     while n > 0:
#         if n % 2 != 0:
#             answer.append("수")
#         else:
#             answer.append("박")
#     return answer

def solution(n):
    answer = []
    if n % 2 == 0:
        k = n // 2
        for i in range(k):
            answer.append("수박")
    else:
        j = n // 2
        for i in range(j):
            answer.append("수박")
        answer.append("수")
    
    result = "".join(map(str, answer))
    return result