# def solution(X, Y):
#     result = []
#     Ylist = list(Y)
#     for i in X:
#         if i in Ylist:
#             result.append(i)
#             Ylist.remove(i)
#     result.sort(reverse =True)
#     if not result:
#         return "-1"
#     elif all(num == "0" for num in result):
#         return "0"
#     else:
#         return "".join(result)

from collections import Counter

def solution(X,Y):
    x = Counter(X) # {'5': 3, '2': 1}
    y = Counter(Y)  # {'1': 1, '2': 1, '5': 2}
    result = []
    
    print(x)
    print(y)
    for num in x:
        if num in y:
            minc = min(x[num], y[num])
            result.extend([num] * minc)
            result.sort(reverse=True)
            
    if not result:  
        return "-1"
    elif result[0] == "0":  
        return "0"
    else:
        return "".join(result)  
            

