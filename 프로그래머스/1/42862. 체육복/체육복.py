# def solution(n, lost, reserve):
#     answer = []
#     cnt = 0
# #번호는 체격순 빌려주는건 양옆만 ㄱㄴ 만약에 숫
#     for i in reserve:
#         answer.append(i-1)
#         answer.append(i)
#         answer.append(i+1)
        
#     if reserve in lost:

def solution(n, lost, reserve):
    real_lost = sorted([i for i in lost if i not in reserve]) 
    real_reserve = sorted([i for i in reserve if i not in lost])


    for i in real_reserve:
        if i - 1 in real_lost: 
            real_lost.remove(i - 1)  
        elif i + 1 in real_lost:  
            real_lost.remove(i + 1)  


    return n - len(real_lost)
 

    return n - len(real_lost)

        

        