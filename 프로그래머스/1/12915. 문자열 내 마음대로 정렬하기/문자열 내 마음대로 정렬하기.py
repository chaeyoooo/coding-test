# def solution(string, n):
#     a = sorted(string, key = lambda x : (x[n] ,x))
#     return a

# def solution(strings, n):
#     result =""
#     for i in strings:
#         result += i[n]
#     newresult = sorted(result)
#     print(newresult)

def solution(strings, n):
    result = [] 
    for i in strings:
        result.append((i[n], i)) 

    newresult = sorted(result) 

    answer = [word for char, word in newresult]  
    return answer