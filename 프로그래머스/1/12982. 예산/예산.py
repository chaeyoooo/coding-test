# from itertools import collection
# def solution(d, budget):
#     # d에 있는 숫자를 하나씩 더 해서 
#     # budget과 가장 가까운 값을 찾고 
#     # 그 값이 몇개냐를 묻는것
#     d.sort()
#     for money in d:
#         if budget >= money:

def solution(d, budget):
    d.sort() 
    count = 0  
    for money in d:
        if budget >= money:  
            budget -= money
            count += 1
        else: 
            break
    return count