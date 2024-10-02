add = [1,2,3,4,5]
print(type(add))

e = [1,2,'Life','is']
print(e[3]+e[2])

a = [1,2,3,['a','b','c']]
print(a[3][1]) # a[3]은 ['a','b','c']이므로 a[3][1]은 'b'가 출력된다
print(a[1][0]) # a[1]은 2이므로 a[1][0]은 오류가 발생한다

#리스트 연산
a =[1,2,3]
b =[4,5,6]
print(a+b) # 리스트 더하기
print(a*3) # 리스트 반복하기
print(len(a)) # 리스트 길이 구하기
print(3+"hi") # 숫자와 문자열은 더할 수 없다 ! 파이썬은 서로 다른 자료형끼리 연산을 할 수 없다

#리스트 수정, 변경, 삭제
a = [1,2,3]
a[2] = 4
print(a) # 리스트 수정

del a[1]
print(a) # 리스트 삭제
del a[1:]
print(a) # 리스트 슬라이싱을 이용한 삭제

#리스트 추가함수
a = [1,2,3]
a.append(4)
print(a) # 리스트에 요소 추가
a.append([5,6])
print(a) # 리스트에 리스트 추가

#리스트 정렬
a = [1,4,3,2]
a.sort()
print(a) # 리스트 정렬

#리스트 뒤집기
a = ['a','c','b']
a.reverse()
print(a) 
print(a.index('a')) # 리스트 요소 위치 반환 a가 몇번쨰 인덱스인지 반환

#리스트 요소 삽입
a = [1,2,3]
a.insert(0,4) # 0번째 인덱스에 4를 삽입
print(a)

#리스트 요소 제거
a = [1,2,3,1,2,3]
a.remove(3) # 리스트 요소 제거
print(a)

#리스트 요소 끄집어내기
a = [1,2,3]
print(a.pop()) # 리스트 요소 끄집어내기 맨 마지막 요소를 끄집어낸다 pop(x)는 x번째 요소를 끄집어낸다
print(a)
print(a.count(1))