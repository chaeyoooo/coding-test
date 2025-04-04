def solution(lottos, win_nums):
    #lottos랑 win_nums를 돌면서 같은거 있는지 확인 하고 num +1
    #그리고 0의 갯수 더해서 cnt 추가하기
    cnt = 0
    zerocnt = 0
    answer =[]
    for i in win_nums:
        if i in lottos:
            cnt +=1 
    if cnt == 1 or cnt == 0:
        answer.append(6)
    elif cnt == 2:
        answer.append(5)
    elif cnt == 3:
        answer.append(4)
    elif cnt == 4:
        answer.append(3)
    elif cnt == 5:
        answer.append(2)
    elif cnt == 6:
        answer.append(1)
        
    for k in lottos:
        if k == 0:
            zerocnt+=1
    
    result = cnt + zerocnt
    
    if result == 1 or result == 0:
        answer.append(6)
    elif result == 2:
        answer.append(5)
    elif result == 3:
        answer.append(4)
    elif result == 4:
        answer.append(3)
    elif result == 5:
        answer.append(2)
    elif result == 6:
        answer.append(1)
        
    answer.sort()

    return answer