def solution(word):
    letters = ['A', 'E', 'I', 'O', 'U']
    count = 0
    answer = 0
    
    def dfs(current):
        nonlocal count , answer
        if current == word:
            answer = count
            return
        if len(current) == 5:
            return
        for ch in letters:
            count +=1
            dfs(current + ch)
    dfs('')
    return answer 