
L = set()
for i in range(1,11):
   a = int(input())
   a = a % 42
   L.add(a)
print(len(L))


# L = []
# for i in range(1,11):
#     a = int(input())
#     Least = a % 42
#     L.append(Least)
# SortedList = set(L)
# print(len(SortedList))