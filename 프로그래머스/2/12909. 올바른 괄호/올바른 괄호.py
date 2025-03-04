def solution(s):
    #")"이게 
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                return False
    return not stack 
        
            