def solution(a, b, n):
    result = 0 
    answer = 0 # a : 마트에 주어야하는 병의 수 , b : a개 가져다주면 마트가 주는 콜라 병의 수
    while n >= a:
        # k = n // a # 20 // 3 : 6
        k = n // a 
        n = n - ( k * a) + (k * b) #내가 가지고 있는 갯수
        answer += (k * b)
    return answer