def solution(number, limit, power):
    #number의 약수를 리스트로 만들고 리스트를 순회하면서 limit을 안넘은 숫자는 
    # replace 안하고 limit을 넘은 숫자는 power로 replace를 한다 그리고 sum을 하면 되겠는데
    #약수 리스트 만들기
    answer = []
    for i in range(1, number +1):
        cnt = 0
        for a in range(1, int(i ** 0.5) + 1):
            if i % a == 0:
                cnt += 1
                if a != i // a:  
                    cnt += 1
                
        answer.append(cnt)
    
    result = []
    for j in range(len(answer)):
        if answer[j] > limit:
            result.append(power)
        else:
            result.append(answer[j])
            
    return sum(result)
            
        