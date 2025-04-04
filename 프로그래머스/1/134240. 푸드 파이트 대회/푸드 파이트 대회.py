def solution(food):
    answer = []
    for i in range(1,len(food)): #1부터 food의 갯수만큼
        if food[i] % 2 != 0: #홀수이면
            k = (food[i]-1)//2
            
        else:
            k = food[i] //2
            
        for j in range(k):
            answer.append(i)
        
    result = answer[::-1]
    answer.append(0)
    answer.extend(result)
    answer = "".join(map(str, answer))
    return answer