def solution(number, k):
    stack = []
    
    for ch in number:
        while stack and k > 0 and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)
    
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)
