def solution(array, commands):
    answer = []
    for i in commands:
        for k in range(len(i)): #i는 [2,5,3]
            result = array[i[0]-1 : i[1]]
            result.sort()
        answer.append(result[i[2]-1])
    return answer