def solution(skill, skill_trees):
    count = 0
    
    #CBD 포함일시 문자열 새로 생성
    for tree in skill_trees:
        s = "" #s를 계속 만듦               
        for i in tree:       
            if i in skill:         
                s += i
                
        # 위치 확인
        if skill[:len(s)] == s:     
            count += 1
    
    return count