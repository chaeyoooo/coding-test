money = int(input())
change = [5,2]
count = 0
for i in change:
   count += money // i
   money = money % i

#여기까지만 접근 했고 
# if (money / 2)  or (money / 5)!= 0:
#    print(-1) 
if money != 0: 
    for i in range(count, -1, -1): 
        money += 5  
        count -= 1  
        if money % 2 == 0:  
            count += money // 2  
            money = 0
            break
# 여기 가운데 코드를 접근 하지 못함 ... ( 5, 2 )

if money == 0:
    print(count)
else:
    print(-1)
