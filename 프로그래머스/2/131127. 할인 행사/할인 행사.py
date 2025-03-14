# def solution(want, number, discount):
#     #want의 배열을 number와 곱해서 리스트로 만들기
#     result = []
#     for i in range(len(want)):
#         result.append(want[i] * number[i])
        
#     print(result)
#     # discount하나씩 땡기면서 비교
#     a = len(discount) - sum(number) # 범위 설정
#     cnt = 0 # 초기 카운트 설정
#     for j in range(a):
#         if result in discount[j:sum(number)]:
#             cnt +=1
#     return cnt

# 리스트로 직접 비교하면 순서 까지 고려해서 false 처리 문제

from collections import Counter
def solution(want, number, discount):
    target = {item: cnt for item , cnt in zip(want, number)}
    
    a = sum(number) #순회횟수
    result = 0
    for j in range(len(discount) - sum(number) + 1):
        window = discount[j:j+a]
        windowcnt = Counter(window)
        
        if windowcnt == target:
            result +=1
        
    return result
        