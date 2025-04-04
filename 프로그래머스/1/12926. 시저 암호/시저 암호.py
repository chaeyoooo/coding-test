def solution(s,n):
    alphabet_lower = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]

    alphabet_upper = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    
    result = []
    index = 0
    newindex =0
    s = list(s) #alphabet_lower, alphabet_upper에서 s에 해당하는거 찾고 인덱스 번호 추출 거기서 #n을 더해서 인덱스 높ㅍ여서 result로 추출
    
    for i in range(len(s)):
        if s[i] in alphabet_lower:
            #alpahbet_lower에 인덱스 번호 찾기 
            index = alphabet_lower.index(s[i])
            newindex = (index + n) % 26 # 새로운 인덱스로 변경
            result.append(alphabet_lower[newindex])
        elif s[i] in alphabet_upper:
            index = alphabet_upper.index(s[i])
            newindex = (index + n) % 26 # 새로운 인덱스로 변경
            result.append(alphabet_upper[newindex])
        #공백있으면
        else:
            result.append(s[i])
    
    return "".join(result)