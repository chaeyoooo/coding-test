a,b = map(int, input().split())
a = list(str(a))
b = list(str(b))
a[0], a[2] = a[2],a[0]
b[0], b[2] = b[2],b[0]
if a > b:
    print(''.join(a))
else:
    print(''.join(b))