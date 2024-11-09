n = 1260
cointypes = [500, 100, 50, 10]
count = 0

for coin in cointypes:
    count+= n//coin
    n%=coin