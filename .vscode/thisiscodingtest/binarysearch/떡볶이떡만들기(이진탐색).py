N,M = map(int,input().split())
tteok = list(map(int, input().split()))

start = 0
end = max(tteok)
result = 0

while start <= end:
    mid = (start + end) //2
    total = 0
    for t in tteok:
        if t > mid:
            total += t - mid
    
    if total >= M:
        result = mid 
        start = mid + 1
    else:
        end = mid -1

print(result)