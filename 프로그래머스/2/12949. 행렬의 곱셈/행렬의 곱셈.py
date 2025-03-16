def solution(arr1, arr2):
    row = len(arr1)# 행의 갯수
    col = len(arr2[0]) #열의 갯수
    line = len(arr1[0]) #arr1의 열의 갯수 , arr2의 행의 갯수
    
    result = [[0] * col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            for k in range(line):
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result
                
