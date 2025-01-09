def router(houses, c , distance):
    count = 1
    last_router = houses[0]
    for i in range(1, len(houses)):
        if houses[i] - last_router >= distance:
            count += 1
            last_router = houses[i]
    return count >=c

n, c = map(int, input().split())
houses = sorted([int(input()) for _ in range(n)])   

start = 1
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    if router(houses, c, mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

