ramenfactory = int(input())
ramen = input().split() # map(int, input().split()) 이랑의 차이 알아야됨
cnt = 0
#연속으로 ramen의 값이 1이 1개 일때 
for i in ramen:
    if ramen == 1:
        cnt +=1
    else:
        cnt = 0

        #어려워서 못풀겠어요 .. 알고보니 다이아 5...

N = int(input())
A = list(map(int,input().split()))+[0, 0]

ans = 0
for i in range(N):
    if A[i+1] > A[i+2]:
        sub = min(A[i], A[i+1]-A[i+2])
        A[i] -= sub; A[i+1] -= sub; ans += sub*5

        sub = min(A[i], A[i+1], A[i+2])
        A[i] -= sub; A[i+1] -= sub; A[i+2] -= sub; ans += sub*7

    else:
        sub = min(A[i], A[i+1], A[i+2])
        A[i] -= sub; A[i+1] -= sub; A[i+2] -= sub; ans += sub*7

        sub = min(A[i], A[i+1])
        A[i] -= sub; A[i+1] -= sub; ans += sub*5

    ans += A[i]*3; A[i] = 0
 
print(ans)
    