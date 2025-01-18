N = list(input())
a = len(N) // 2 

cnt1 = 0
for i in range(a):
     cnt1 += int(N[i])

cnt2= 0

for j in range(a+1,len(N)):
    cnt2 += int(N[j])

if cnt1 == cnt2:
     print("LUCKY")
else:
     print("READY")
