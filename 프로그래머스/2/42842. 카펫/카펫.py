def solution(brown, yellow):
    #일단 brown + yellow 를 더 해서 약수 찾기
    whole = brown + yellow
    
    #약수 찾기 
    result = []
    for i in range(1, whole+1):
        if whole % i == 0:
            j = whole // i
            if i >= j:
                result.append((i, j)) #튜플로 분해
            
    for x , y in result:
        if (x -2) * (y-2) == yellow:
            return [x,y]
        