class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit() # Unit 생성자만 호출됨 , 다중 상속의 경우 맨 처음에 상속받는 클래스의 생성자만 호출됨 , 따라서 각자 클래스의 생성자를 호출해줘야함