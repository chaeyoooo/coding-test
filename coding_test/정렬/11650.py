N = int(input())
a = []
for _ in range(N):
    x,y = list(map(int, input().split()))
    a.append((x,y))

# print(a)

if a:
    a.sort(key=lambda x: (x[0], x[1]))

# print(a)

for i in a:
    print(i[0], i[1])


