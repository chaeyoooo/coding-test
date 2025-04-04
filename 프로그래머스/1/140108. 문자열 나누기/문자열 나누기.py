def solution(s):
    answer = 0
    countsame, countdiff = 0,0
    x = ''
    
    for char in s:
        if x == '':
            x = char
            
        if char == x:
            countsame +=1
        else:
            countdiff +=1
        
        if countsame == countdiff:
            answer +=1
            x = ''
            countsame, countdiff = 0, 0
    return answer + (1 if x else 0)