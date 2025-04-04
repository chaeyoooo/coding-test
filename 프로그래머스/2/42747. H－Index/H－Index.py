# def solution(citations):
#     cnt = 0
#     for i in citations:
#         for k in range(len(citations)):
#             if i >= k:
#                 cnt +=1
            
#     if cnt == k:
#         return cnt
def solution(citations):
    citations.sort(reverse = True) #내림차순 정렬 #[6,5,3,1,0]
    
    for i, citation in enumerate(citations):
        if citation < i+1:
            return i
    
    return len(citations)
        

# 논문 n편중 h번 이상 인용된 논문이 h편 이상 이고 나머지 논문이 h번 이하, 
#만약에 len(citations)을 돌고 이게 1이상이면 3번 , 1이하면 2번 / 2이상이면 3, 
#2이하이면 4번 , 2이하이면 2번 / 3이상이면 3번 , 3이면 2번 / 4이상이면 2번 , 4이면 3번데

