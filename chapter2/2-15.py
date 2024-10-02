#머란 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린"
hp = 40
damage = 5

print(f"{name} 유닛이 생성 되었습니다")
print(f"체력: {hp} , 공격력: {damage}\n")

#탱크 : 공격유닛, 탱크 , 포를 쓸 수 있는데 일반모드/ 시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print(f"{tank_name} 유닛이 생성 되었습니다")
print(f"체력: {tank_hp} , 공격력: {tank_damage}\n")

#탱크 : 공격유닛, 탱크 , 포를 쓸 수 있는데 일반모드/ 시즈모드
tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print(f"{tank2_name} 유닛이 생성 되었습니다")
print(f"체력: {tank2_hp} , 공격력: {tank2_damage}\n")

def attack(name, location, damage):
    print(f"{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage}]")

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 이렇게  중복해서 반복할 수 없으니까 클래스를 사용하자

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 멤버변수
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다")
        print(f"체력: {self.hp} , 공격력: {self.damage}\n")

marin1 = Unit("마린", 40, 5) #마린은 객체 생성 (클래스로 부터 만들어지는 녀석들) 또한 유닛 클래스의 인스턴스
marin2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중유닛, 비행기, 클로킹(상대방에게 보이지 않음)
race1 = Unit("레이스", 80, 5)
print(f"유닛 이름: {race1.name}, 공격력: {race1.damage}") # 외부에서 멤버변수에 접근 가능

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
race2 = Unit("레이스", 80, 5)
race2.clocking = True # 외부에서 멤버변수 추가 가능

if race2.clocking == True:
    print(f"{race2.name} 는 현재 클로킹 상태입니다.")