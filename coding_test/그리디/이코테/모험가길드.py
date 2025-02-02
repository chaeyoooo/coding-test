n = int(input()) #모험가의 수
fear = map(int,input().split()) # 공포도

fear = set(fear)
fear_cnt = len(fear)
fear_sum = sum(fear)

if fear_sum == n:
    print(fear_cnt)
else:
    print(fear_cnt-1)
    