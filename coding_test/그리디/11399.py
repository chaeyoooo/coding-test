n = int(input())
time = list(map(int, input().split()))
time.sort()
a = []
for i in range(n):
    a.append(time[i] * (n-i))
print(sum(a))

# 5
# 3 1 4 3 2

# 32

# 3  >3
# 3+1 >4
# 3+1+4  >10
# 3+1+4+3 >13
# 3+1+4+3+2 >15