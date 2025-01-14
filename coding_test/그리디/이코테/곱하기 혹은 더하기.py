s = input()
answer = 0

#하나씩 접근
for i in s:
    if int(i) <=1 or answer <=1:
        answer += int(i)
    else:
        answer *= int(i)

print(answer)