
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 멤버변수
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다")
        print(f"체력: {self.hp} , 공격력: {self.damage}\n")

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name # 멤버변수
        self.hp = hp
        self.damage = damage

    def attack(self, location): #메소드 앞에는 무조건 self를 적어줘야함
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)