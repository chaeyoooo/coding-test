def solution(n, arr1, arr2):
    result = []
    
    for i in range(n):
        a = bin(arr1[i])[2:].zfill(n)
        b = bin(arr2[i])[2:].zfill(n)
        
        row = ""
        for j in range(n):
            if a[j] == "1" or b[j] == "1":
                row += "#"
            else:
                row += " "
                
        result.append(row)
                
    return result

# def solution(n, arr1, arr2):
#     stack1 = []
#     k = 0
#     for i in arr1:
#         k = i % 2 # 9 를 2로 나눴을 때 나머지
#         stack1.append(k)
#         i = i // 2
    
#     return stack1
        
        