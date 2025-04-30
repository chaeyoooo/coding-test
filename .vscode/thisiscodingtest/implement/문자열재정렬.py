S = input()

letters = []
digit = 0

for c in S:
    if c.isalpha():
        letters.append(c)
    elif c.isdigit():
        digit += int(c)

letters.sort() # 리스트만!

if digit > 0:
    letters.append(str(digit))

print("".join(letters)) #리스트 안에 있는 문자열을 하나로 합치는 것!