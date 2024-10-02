absent = [2, 5] # 결석
no_books = [7] # 책을 깜빡함
for stundent in range(1,11):
    if stundent in absent:
        continue  # continue를 만나면 아래 코드를 실행하지 않고 다음 반복으로 넘어간다.
    elif stundent in no_books:
        print(f"오늘 수업 여기 까지 {stundent}는 교무실로 따라와")
        break # break를 만나면 반복문을 종료한다.
    print(f"{stundent}" "책을 읽어봐")



