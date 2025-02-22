def solution(answers):
    result1 = [1,2,3,4,5] * ((len(answers) // 5)+1)
    result2 = [2,1,2,3,2,4,2,5] * ((len(answers) //8)+1)
    result3 = [3,3,1,1,2,2,4,4,5,5] * ((len(answers)// 10)+1)
    
    cnt1 =0
    cnt2 =0
    cnt3 =0
    for i in range(len(answers)):
        if answers[i] == result1[i]:
            cnt1 += 1
        if answers[i] == result2[i]:
            cnt2 +=1
        if answers[i] == result3[i]:
            cnt3 +=1
            
    if cnt1 == cnt2 == cnt3:
        return [1,2,3]
    
    maxscore = max(cnt1, cnt2, cnt3)
    answer = []
    
    if cnt1 == maxscore:
        answer.append(1)
    if cnt2 == maxscore:
        answer.append(2)
    if cnt3 == maxscore:
        answer.append(3)
        
    return answer
        
    
    
    