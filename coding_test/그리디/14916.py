# money = int(input())
# change = [5,2]
# count = 0
# for i in change:
#    count += money // i
#    money = money % i

#여기까지만 접근 했고 
# if (money / 2)  or (money / 5)!= 0:
#    print(-1) 
# if money != 0: 
#     for i in range(count, -1, -1): 
#         money += 5  
#         count -= 1  
#         if money % 2 == 0:  
#             count += money // 2  
#             money = 0
#             break
# # 여기 가운데 코드를 접근 하지 못함 ... ( 5, 2 )

# if money == 0:
#     print(count)
# else:
#     print(-1)

# n = int(input())

# cnt = 0
# i = 0
# while True:
#     if n % 5 == 0:   # 5의배수이면 or 2로만 거슬러주고 n이 0이된경우 
#         cnt += n//5		#5로나눈 몫이 정답 
#         break
#     else:
#         n -= 2   #5의배수가 아니면 2백원씩 뺴면서 5로 나누어떨어지는것이 나오도록
#         cnt += 1

#     if n < 0:  # 2백원씩 뺏더니 음수가 되버린경우 --> 거슬러줄수 없을을 의미함 
#         break
# if n<0:			# 음수면 거슬러줄수없 
#     print(-1)			
# else:
#     print(cnt)

money = int(input()) #13
cnt = 0

while True:
    if money % 5 == 0:
        cnt += money // 5
        break
    else:
        money -= 2
        cnt += 1

    if money < 0:
        break
if money < 0:
    print("-1")
else:
    print(cnt)


