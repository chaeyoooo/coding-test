def solution(s):
    change = 0
    zero = 0
    while s != "1":
        cnt = s.count("0")
        zero += cnt
        
        s = s.replace("0" , "")
        
        s = bin(len(s))[2:]
        change += 1
        
    return [change , zero]
   
    