realcoin = int(input())
coin = 1000-realcoin
count = 0
coin_list = [500, 100, 50 , 10 ,5,1 ]
for i in coin_list:
    count += coin // i
    coin %= i
print(count)