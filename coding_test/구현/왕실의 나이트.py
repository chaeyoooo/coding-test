inputdata = input()
row = int(inputdata[1])
colums = int(ord(inputdata[0])) - int(ord("a")) + 1

steps = [(-2,-1) , (-1, -2) , (1, -2) , (2, -1), (2, 1), (1, 2) , (-1, 2), (-2, 1)]

result = 0
for step in steps:
    nextrow = row + step[0]
    nextcolums = colums + step[1]

    if nextrow >=1 and nextrow <=8 and nextcolums >=1 and nextrow <= 8:
        result +=1

print(result)