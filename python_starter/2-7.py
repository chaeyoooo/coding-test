#한줄 for문
students = [1,2,3,4,5]
print(students)
students =[i+100 for i in students] # students에 있는 요소들을 i로 받아와서 i+100을 한 값을 다시 students에 넣어준다
print(students)

students = ["아이언맨", "토르", "그루트"]
students =[len(i) for i in students] # students에 있는 요소들을 i로 받아와서 i의 길이를 구한 값을 다시 students에 넣어준다
print(students)

students =["ironman , thor, groot"]
students =[i.upper() for i in students]
print(students)