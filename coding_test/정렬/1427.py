a = list(map(int, input())) 
a.sort(reverse=True)
print(a)
print(''.join(map(str, a)))