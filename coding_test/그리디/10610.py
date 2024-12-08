#일단 n이 5째자리 까지 가능함
# n이 1일때 그냥 3의 배수인지 확인하고 3의 배수가 아니면 -1 출력
# n이 2이상일때는 30의 배수인지 확인하고 30의 배수가 아니면 -1 출력
# n이 3이상일때는 300의 배수인지 확인하고 300의 배수가 아니면 -1 출력
# n이 4이상일때는 3000의 배수인지 확인하고 3000의 배수가 아니면 -1 출력
# n이 5이상일때는 30000의 배수인지 확인하고 30000의 배수가 아니면 -1 출력

# n = 150
# print(len(str(n)))

# n = int(input())
# if len(str(n)) == 1:
#     if n % 3 == 0:  # '=' 대신 '==' 사용
#         print(n)
#     else:
#         print(-1)
# elif len(str(n)) == 2:
#     if n % 30 == 0:  # '=' 대신 '==' 사용
#         print(n)
#     else:
#         print(-1)
# elif len(str(n)) == 3:
#     if n % 300 == 0:  # '=' 대신 '==' 사용
#         print(n)
#     else:
#         print(-1)
# elif len(str(n)) == 4:
#     if n % 3000 == 0:  # '=' 대신 '==' 사용
#         print(n)
#     else:
#         print(-1)
# elif len(str(n)) == 5:
#     if n % 30000 == 0:  # '=' 대신 '==' 사용
#         print(n)
#     else:
#         print(-1)
# else:
#     print(-1)

# 30이 조건이니까 각 자릿수의 합이 3의 배수이면서 각자리 수에 0이 포함되어 있어야함!
# 30의 배수가 아니면 -1 출력

n = str(int(input()))
n = sorted(n,reverse=True) # sorted 함수는 무조건 문자열로만 반환 되기에 리스트를 문자열로 바꿔주어야함!
k = sum(map(int, n))
if k % 3 ==0 and '0' in n:
    print("".join(n))
else:
    print(-1)

#여기서 빼먹은게 내림차순으로 정렬을 해야됨
#'0' in n 이거는 0이 n에 포함되어 있으면 True 아니면 False
#"".join(n) 이거는 리스트를 문자열로 바꿔주는 함수
#k = sum(map(int, n)) 이거는 n의 각 자리수를 int로 바꾸고 다 더해주는 함수
