# def solution(left, right):
#     cnt = 0
#     answer = list(range(left, right+1))
#     for i in answer:
#         for k in range(1, answer[i]):
#             if i % k == 0:
#                 cnt +=1
#             return cnt

def solution(left, right):
    result = 0
    for i in range(left, right+1):
        count = 0
        for s in range(1, i+1):
            if i % s == 0:
                count +=1
        if count % 2 == 0:
            result += i
        else:
            result -= i
    return result