# from collections import Counter
# def solution(k, tangerine):
#     #[1,3,2,5,4,5,2,3] #1은 1개 2는 2개 3은 2개 4는 1개 5는 1개 
#     cnt_t = Counter(tangerine) # 각 요소 등장횟수 세서 딕셔너리 형태 !
#     print(cnt_t)
    
#     cnt = 0
#     for i , j in counter:
#         cnt += j 
#         if cnt == k:
#             break
#         elif cnt > k:
#             #i의 갯수

from collections import Counter

def solution(k, tangerine):
    #[1,3,2,5,4,5,2,3] #1은 1개 2는 2개 3은 2개 4는 1개 5는 1개 
    cnt_t = Counter(tangerine) # 각 요소 등장횟수 세서 딕셔너리 형태 !
    
    cnt = 0 # 귤 갯수 누적
    unique = 0 # 하나씩 증가 
    cnt_tt = sorted(cnt_t.items(), key = lambda x :x[1] , reverse = True)
    for i, j in cnt_tt:  
        cnt += j 
        unique +=1
        if cnt >= k:
            return unique
        

            
        
        