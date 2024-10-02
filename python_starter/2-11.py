#가변인자
def profile(name, age, *language): #가변인자를 사용하려면 *을 사용한다.
    print(f"이름: {name}\t나이: {age}\t 언어:{language}") #end=" " 사용하면 줄바꿈을 하지 않고 이어서 출력한다.
    # for lang in language:
    #     print(lang , end=" ")

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")
