N,M = map(int, input().split())
tteok = list(map(int, input().split()))

j = 1
while True:
    sum =0
    for i in range(len(tteok)):
        if tteok[i] - j >0:
            sum += (tteok[i] - j)

    if sum == M:
        print(j)
        break
    
    j+=1