def solution(prices):
    stack = []

    for i in range(len(prices)):
        count = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break
        stack.append(count)
    return stack


# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         cnt = 0
#         prev = prices[i] #1
#         next = prices[i+1:] #2,3,2,3
        
#         for j in range(len(next)):
#             if prev <= next[j]:
#                 cnt+=1
#             else:
#                 cnt+=1
#                 break
            
#         answer.append(cnt)
#     return answer


# def solution(prices):
#     answer = []
#     cnt = 0
#     for i in range(len(prices)): 
#         cnt = 0
#         for j in range(i + 1, len(prices)): 
#             if prices[i] >= prices[j]: 
#                 cnt += 1 
#                 break
#             else:
#                 cnt += 1
        
#         answer.append(cnt) 
        
#     return answer
