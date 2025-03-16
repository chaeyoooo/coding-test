from collections import Counter
def solution(clothes):
    count_gory = Counter(category for name , category in clothes) #카테고리만 세는 카운터
    
    answer = 1
    for  category , cnt in count_gory.items():
        answer *= (cnt+1)
    return answer -1
        
        
    
        