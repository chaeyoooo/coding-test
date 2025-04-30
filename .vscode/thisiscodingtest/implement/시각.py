n = int(input())

cnt = 0

for i in range(0, n+1):
    for k in range(0,61):
        for j in range(0, 61):
            if '3' in str(i) + str(k) + str(j):
                cnt +=1
    
# 여기서 잘못한게 3이어야 cnt를 올리는게 아니라 13,30과 같으면 cnt를 증가 시켜야하기에 
# 문자열로 만들고 포함되어 있어야함!
print(cnt)