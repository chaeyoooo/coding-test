#반복문
N = int(input())

result = 1

for i in range(1,N):
    result *= i

print(result)

#팩토리얼
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)