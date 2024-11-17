a = int(input())
for i in range(a):
    b ,c = input().split()
    b = int(b)
    result = ''.join([b*char for char in c])
    print(result)