def solution(absolutes, signs):
    answer = []
    #sign의 true 인덱스 가져오기
    for i in range(len(signs)):
        if signs[i] == True:
            answer.append(absolutes[i])
        else:
            answer.append(-absolutes[i])
    return sum(answer)