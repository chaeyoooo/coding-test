def solution(n, words):
  
    #알파벳이 끊어지지 않거나 똑같은 단어
    #먼저 탈락하는 사람의 번호 / 그 사람이 자신의 몇번째 차례에 탈락 하는지
    
    for i in range(1, len(words)):
        if (words[i][0] != words[i-1][-1]) or (words[i] in words[:i]):
            return [(i%n)+1 , (i//n) + 1]
    return [0,0]
        