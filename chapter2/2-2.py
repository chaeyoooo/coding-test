# 문자열 연산
head = "Python"
tail = " is fun!"
print(head + tail)

a = "Python"
print(a * 2) # 문자열 곱하기
len(a) # 문자열 길이

a = "Life is too short, You need Python"
print(a[0] + a[1] + a[2] + a[3]) # 문자열 인덱싱 하면 하나의 문자만 가져옴
print(a[0:4]) # 문자열 슬라이싱 하면 범위만큼 가져옴 [시작 : 끝 : 범위]
print(a[::2]) # 2칸씩 건너뛰기
print(a[::-3]) # 역순으로 3칸씩 건너뛰기

#문자열 포매팅
number = 10
day = "three"
a = "I eat %d apples so I was sick %s times" % (number, day)
print(a)

name = "홍길동"
age = 30
a = f"나의 이름은 {name}입니다. 나이는 {age+1}입니다."
print(a)

# 문자열 갯수 세기
a = "hobby"
print(a.count('b')) # 문자열에서 b의 개수

# 문자열 위치 알려주기
a = "Python is the best choice"
print(a.find('b')) # 문자열에서 b가 처음 나온 위치
print(a.find('k')) # 없는 문자를 찾으면 -1 반환

# 문자열 위치 알려주기
a = "Python is the best choice"
print(a.index('b')) # 문자열에서 b가 처음 나온 위치
print(a.index('k')) # 없는 문자를 찾으면 오류 발생

# 문자열 삽입
a = "," .join('abcd')
print(a)

# 소문자를 대문자로 바꾸기
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기
a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기
a = " hi "
print(a.rstrip())

# 양쪽 공백 지우기
a = " hi "
print(a.strip())

# 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))
print(a.split()) # 공백을 기준으로 문자열 나누기