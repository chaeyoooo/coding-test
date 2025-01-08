age = int(input())
list = []
for i in range(age):
    a,b = input().split()
    list.append((a,b))

list.sort(key = lambda x: int(x[0]))

for i in list:
    print(i[0], i[1])
