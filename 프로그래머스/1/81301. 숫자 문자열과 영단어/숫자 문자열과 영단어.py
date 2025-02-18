def solution(s):
    alphabet ={ "zero" : 0 ,"one" : 1 , "two" : 2 ,  "three" :3 , "four" : 4 , "five" :5 , "six" : 6 , "seven" : 7 , "eight" : 8 , "nine" : 9}
    
    answer = ""
    #딕셔너리에서 key, value가져오는것
    for word , number in alphabet.items():
        s = s.replace(word , str(number))
    
    
    return int(s)