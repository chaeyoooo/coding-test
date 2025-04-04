# def solution(scoville, K):
# # 매운 것을 좋아하는 레오는 모든 음식의 스코빌 지수를 k 이상으로 만들고 싶다 .
# # 자 그러면 스코빌 지수가 가장 낮은 두개의 음식을 섞어서 새로운 음식을 만들려고 함
# # 섞은 음식 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수  + 두번쨰로 맵지 않은 스코빌 지수 * 2 

# #일단 모든 숫자가 K 이상이면 ㅇㅋ
#     cnt = 0 
#     while scoville[0] < K:
#         if len(scoville) == 1 and scoville[0] < K: #두개가 안된거니까
#             return -1
#         scoville.sort()
#         first = scoville[0] #0번 인덱스를 사용해서 가장 최솟값
#         second = scoville[1] #1번 인덱스를 사용해서 두번째 최솟값
    
#         new = first + (second * 2)
#         scoville = [new] + scoville[2:]
#         cnt += 1
#     return cnt

import heapq
def solution(scoville, K):
    heapq.heapify(scoville) #힙으로 변환
    cnt = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        cnt +=1
        
    return cnt
    