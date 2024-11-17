s = input()
result = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in alphabet:
    result.append(s.find(char))
print(' '.join(map(str, result)))

#string.find(substring)
#문자열에서 특정 문자열을 찾아서 그 위치를 반환한다.
# 만약 substring이 string에 존재하지 않으면 -1을 반환합니다.