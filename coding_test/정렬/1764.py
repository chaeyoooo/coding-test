N , M = map (int, input().split())  

no_hear =[]
no_see = []

for _ in range(N):
    no_hear.append(input())

for _ in range(M):
    no_see.append(input())


no_hear_set = set(no_hear)
no_see_set = set(no_see)


result = sorted(list(no_hear_set&no_see_set))

print(len(result))
for i in result:
    print(i)
