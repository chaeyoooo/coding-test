def solution(name, yearning, photo):
    answer = []
    #일단 photo를 돌면서 name이 있는지 없는지 확인 
    for i in range(len(photo)):
        sum = 0
        for j in range(len(name)):
            if name[j] in photo[i]:
                sum += yearning[j]
                
        answer.append(sum)
        
    return answer