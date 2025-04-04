# def solution(s, skip, index):
#     #a에서 +1 ~+5까지 구하고 여기 리스트에 skip에 포함된거 제외 하고 그 숫자만큼 +6, +7 하고 맨 마지막값
#     #먼저 s를 돌면서 왼쪽 부터 하나씩 뽑음
#     hello =[]
#     for i in s:
#         newchar = i
#         temp = [] #초기화 시켜줌으로써 과정출력
#         for j in range(1, index+1):
#             newchar = (chr((ord(i) -97 + j) % 26 + 97))
#             temp.append(newchar)
        
#         for i in range(len(temp)):
#             if temp[i] == skip:
#                 hello.append(i)

def solution(s, skip, index):
    hello = []
    
    for i in s:
        newchar = i  
        step = 0  

        while step < index:  
            newchar = chr((ord(newchar) - 97 + 1) % 26 + 97)  
            if newchar not in skip:  
                step += 1
        
        hello.append(newchar) 

    return "".join(hello)

                
        
        
    
        