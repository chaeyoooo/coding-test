# 만약 4의 배수가 아니면 1을 빼고 만약 4의 배수이면 4로 나눈다
a, b = map(int, input().split())

count = 0
while a != 1:
    if a % b != 0:
        a = a -1
        count +=1
    else:
        a = a // b
        count +=1
print(count)