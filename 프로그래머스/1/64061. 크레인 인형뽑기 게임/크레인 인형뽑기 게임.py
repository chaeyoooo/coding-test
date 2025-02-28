def solution(board, moves): # 사라진 인형의 갯수 return 하는 방식
    answer = []
    columns = list(zip(*board))
    newboard = []
    newmoves = []
    for row in columns:
        newboard.append(list(row))
        
    for k in moves:
        newmoves.append(k-1)
        
    for i in newmoves:
        for j in range(len(newboard[i])):
            if newboard[i][j] == 0:
                continue
            else:
                answer.append(newboard[i][j])
                newboard[i][j] = 0
                break #하나만 뽑아야하니까
    cnt = 0
    for i in range(len(answer)-1, 0 , -1 ): #뒤에서 부터 비교 , pop()으로 인덱스 달라지는거 방지
        if i < len(answer) and answer[i] == answer[i-1]:
            answer.pop(i)
            answer.pop(i-1)
            cnt += 2
            
    return cnt 