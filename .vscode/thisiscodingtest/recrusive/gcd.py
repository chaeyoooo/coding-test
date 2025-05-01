# 나머지가 아닌 빼기로 풀이
def gcd(a,b):
    while a!= 0 and b!= 0:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a+b

# 반복문
def gcd(a,b):
    while b!= 0:
        a,b = b, a % b
    return a

#재귀함수
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
