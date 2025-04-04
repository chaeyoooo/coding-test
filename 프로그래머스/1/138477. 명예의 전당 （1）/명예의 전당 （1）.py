# 힙 사용
import heapq

def solution(k , score):
    result = []
    answer = []
    for i in score:
        heapq.heappush(result , i)
        
        if len(result) > k:
            heapq.heappop(result)
            
        answer.append(result[0])
        
    return answer



# def solution(k, score):
#     answer = []
#     for i in score:
#         answer.append(i)
#         sorted(answer)
#         while 
#     return answer