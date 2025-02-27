# def solution(keymap, targets):
#     dict = {}
#     #keymap중에 target에 해당하는게 있으면 index번호 min가져오고 이걸 더 하는 방식으로
#     for i in keymap:
#         for num , char in enumerate(i):
#             if char not in dict: #비어있다면
#                 dict[char] = num
#             else: #중복된다면
#                 dict[char] = min(dict[char] , num)
                
#     print(dict)
#     cnt = 0
#     answer = []
#     for k in targets:
#         result = []
#         for j in k :
#             if j in dict:
#                 result.append(dict[j])
        
#             else:  
#                 result = [-1]
#                 answer.append(result)
#                 break
#         else:
#             answer.append(result)
#     print(answer) #배열 2개가 나와야됨
    
#     realanswer = []
#     if not any (answer): #배열 비어있으면
#         return [-1]
#     for k in answer:
#         realanswer.append(sum(k) + len(k))
        
#     return realanswer

def solution(keymap, targets):
    key_dict = {}  

    for i in keymap:
        for num, char in enumerate(i):
            if char not in key_dict:
                key_dict[char] = num + 1  
            else:
                key_dict[char] = min(key_dict[char], num + 1)

    answer = []

    for k in targets:
        result = []
        for j in k:
            if j in key_dict:
                result.append(key_dict[j])
            else:
                answer.append(-1)  
                break
        else:
            answer.append(sum(result))  

    return answer



            
            
                