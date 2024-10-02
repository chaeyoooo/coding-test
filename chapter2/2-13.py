print("Python" , "Java" , sep=",", end ="?") #이 줄에 마지막에?를 넣고 줄바꿈 ㄴ
print("무엇이 더 재밌을까요?")
print("Python" , "Java" , sep=" vs ")

#출력 포멧
scores = {"수학": 0 , "영어": 50, "코딩":100}
for subjects, score in scores.items():
    # print(subjects,score)
    print(subjects.ljust(8), str(score).rjust(4), sep=":") #8칸 공간 확보한 뒤에 왼족 정렬 / 4개 공간 확보한 뒤에 오른쪽 정렬


#은행  대기 순번표
for num in range(1,21):
    print("대기번호: " + str(num).zfill(3)) # 3개의 크기 만큼 집어넣고 없는 자리에 0 집어넣는것

answer = input("아무값이나 입력하세요 : ")
print(f"입력하신 값은 {answer} 입니다")