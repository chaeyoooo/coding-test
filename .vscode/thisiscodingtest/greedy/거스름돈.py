n = 1260

types = [500,100, 50 ,10]

count = 0
for coin in types:
    count += n // coin
    n = n % coin

print(count)