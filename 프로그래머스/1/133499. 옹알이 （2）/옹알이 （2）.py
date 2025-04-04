def solution(babbling):
    joka = ["aya" , "ye" , "woo" , "ma"]
    cnt = 0
    
    for i in babbling:
        for j in joka:
            if j * 2 in i:
                break
            i = i.replace(j,"X")
            
        if i.replace("X" , "") == "":
            cnt += 1
        
    return cnt
