
L = set()
for i in range(1,11):
   a = int(input())
   a = a % 42
   L.add(a)
print(len(L))

# 집합은 중복을 허용하지 않는다. 따라서 중복된 값은 제거된다.

# L = []
# for i in range(1,11):
#     a = int(input())
#     Least = a % 42
#     L.append(Least)
# SortedList = set(L)
# print(len(SortedList))