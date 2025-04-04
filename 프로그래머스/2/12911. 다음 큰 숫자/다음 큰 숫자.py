# def solution(n):
#     #n의 다음 큰 숫자는 n보다 큰 자연수
#     #n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수 같음
    
    
#     #그러면 n을 하나씩 증가 시키고 n을 2진수로 바꿨을 때 1의 갯수 랑 하나씩 증가시킨후 2의 진수로 바꾸고
#     #1의 갯수로 바꾸면 답 나옴
#     stack = []
#     num = n # 원래 값 저장
#     while num > 0:
#         stack.append(n % 2)
#         num = num // 2
    
#     a = stack[::-1]
#     cnt1 = 0
#     for i in a:
#         if i == 1:
#             cnt1 +=1
    
#     next = n+1
#     while True:
#         stack = []
#         num = next
#         while num > 0:
#             stack.append(n % 2)
#             num = num // 2
    
#     b = stack[::-1]
    
#     for i in b:
#         if i == 1:
#             cnt2 +=1
            
#     if cnt == cnt2:
#         return next

def solution(n):
    answer = n+1
    ones_count = bin(n)[2:].count('1')
    while True:
        if ones_count == bin(answer)[2:].count('1'):
            return answer
        else:
            answer += 1
        

    
    
    
    
    