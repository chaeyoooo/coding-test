# from itertools import combinations
# def solution(k, m, score): 
#     answer = 0
#     #k는 최상품의 사과 / m 은 한상자에 들어가는 사과의 수 / 
#     #score을 정렬한다음에 맨뒤에서 부터 3개를 뽑기 !
#     for i in combinations(score, m):
#         for k in range(len(i)):
#             answer += min(i[k]) * m
#     print(answer)

def solution(k, m, score): 
    answer = 0
    score.sort(reverse=True)  

    for i in range(0, len(score), m): 
        if i + m <= len(score):  #i에서 m개를 뽑아도 리스트 안에 남아있는 경우
            answer += min(score[i:i+m]) * m  

    return answer