# # n = int(input())
# # circle = []
# # circle.append("(")
# # circle.pop(")")

# # if circle is empty:
# #     print("YES")
# # else:
# #     print("N0")

# n = int(input())
# for _ in range(n):
#     ps = input()
#     circle = []

#     for char in ps:
#         if char == "(":
#             circle.append("(")
#         elif char == ")":
#             if circle: # if문 쓴 이유는 circle이 비어있으면 오류남 , 스택 비어있지 않으면
#                 circle.pop()
#             else:
#                 break

#     if not circle:
#         print("YES")
#     else:
#         print("NO")

# 이렇게 되면 잘못된 기호가 나오면 바로 반복문을 멈추지만 , 이 방식은 문자열 전체를 처리하지
# 않고 바로 종료 하기 때문에 결과가 어긋날 수 있다 ..!

n = int(input())
for _ in range(n):
    ps = input()
    circle = []
    is_valid = True  # 기본값은 올바른 괄호 문자열(VPS)

    for char in ps:
        if char == "(":
            circle.append("(")  # 열린 괄호 추가
        elif char == ")":
            if circle:  # 스택에 열린 괄호가 있으면 제거
                circle.pop()
            else:
                is_valid = False  # 짝이 맞지 않는 경우
                break  # 문자열 전체를 볼 필요 없이 중단

    # 문자열 끝난 후 스택 상태 확인
    if is_valid and not circle:
        print("YES")
    else:
        print("NO")

