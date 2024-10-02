# for 반복문
print("대기번호 :1")
print("대기번호 :2")
print("대기번호 :3")
print("대기번호 :4")

for waiting_no in [0, 1, 2, 3, 4]:
    print(f"대기번호 : {waiting_no}")

for waiting_no in range(5): #0부터 5미만의 숫자
    print(f"대기번호 : {waiting_no}")

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print(f"{customer}, 커피가 준비되었습니다.")

# while문
customer = "토르"
index = 5
while index >=1:
    print(f"{customer}, 커피가 준비되었습니다. {index}번 남았어요")
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
Index = 1
while True:
    print(f"{customer}", "커피가 준비 되었습니다. 호출 {Index}회")
    Index += 1

customer = "토르"
person = "Unknown"

while person !=customer:
    print(f"{customer}, 커피가 준비되었습니다.")
    person = input("이름이 어떻게 되세요?")

# 만약 person이 토르면 반복문이 종료된다.
