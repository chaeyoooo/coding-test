# def solution(order):
#     ordered = sorted(order)
#     stack = []
#     truck = []
#     for i in ordered:
#         if i == order[0]:
#             truck.append(order[0])
#             ordered.pop(order[0])
#         else:
#             stack.append(ordered[i])
        
#     stack = stack[::-1]
#     ordered = ordered[::-1]
#     for i in ordered:
        

# def solution(order):
#     ordered = []
#     stack = []
#     trunk = []
#     for i in range(1, len(order)+1):
#         ordered.append(i)
#     print(ordered)
    
#     for i in ordered:
#         if i == order[0]:
#             trunk.append(order[i])
#         else:
#             stack.append(i)
            
            
def solution(order):
    ordered = []
    stack = []
    trunk = []
    idx = 0  # 현재 order에서 실어야 할 인덱스

    for i in range(1, len(order)+1):
        ordered.append(i)

    for i in ordered:
        if i == order[idx]:
            trunk.append(i)
            idx += 1
            while stack and stack[-1] == order[idx]:
                trunk.append(stack.pop())
                idx += 1
        else:
            stack.append(i)

    return len(trunk)


