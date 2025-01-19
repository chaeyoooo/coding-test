N = input()

letters = []
numbers = []

for char in N:
    if char.isalpha():
        letters.append(char)
    elif char.isdigit():
        numbers.append(int(char))

letters.sort()
total = sum(numbers)

result = ''.join(letters) + str(total)

print(result)