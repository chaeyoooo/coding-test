gun =10

def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print(f"[함수 내] 남은 총: {gun}")

print(f"전체 총: {gun}")
checkpoint(2)
print(f"남은 총: {gun}")

# 전체 총: 10
# [함수 내] 남은 총: 18
# 남은 총: 10
# 전역변수 gun은 10이지만 함수 내에서 gun이 20으로 재할당 되어 18이 출력된다. 그리고 함수 밖에서 gun은 10이니까 전체총과 남은 총은 10이 출력된다
# 이런 문제를 해결하기 위해선 함수 내에서 gun이 전역변수임을 명시해야한다. 전역변수 잘 안쓰는게 좋다.

gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print(f"[함수 내] 남은 총: {gun}")

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(f"[함수 내] 남은 총: {gun}")
    return gun

print(f"전체 총: {gun}")
gun = checkpoint_ret(gun, 2)
print(f"남은 총: {gun}")