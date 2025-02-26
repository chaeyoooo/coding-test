def solution(ingredient):
    # a = "".join(map(str, ingredient))
    # answer = 0
    # while "1231" in a:
    #     answer += 1
    #     a = a.replace("1231" , "")
    # return answer
    
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            del stack[-4:]
        
    return answer