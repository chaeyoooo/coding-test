#처음에 일단 리스트로 3,5 주고
# 5로 먼저 나눠지는 지 확인하고 몫이 cnt ! 그리고 그 숫자가 5로 나눠지지 않으면 -3을 하고 다시 cnt + 1
#cnt출력

n = int(input())
cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    n -= 3
    cnt += 1
else:
    print(-1)

# 먼저 -3을 하고 난다음에 5로 나눠지는지 확인하는 구조