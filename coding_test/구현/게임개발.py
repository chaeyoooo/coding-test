#입력
n, m = map(int, input().split())
x,y,direction = map(int, input(). split())

# 2차원 배열 입력받기
mapp =[]
for _ in range(n):
    mapp.append(list(map(int, input().split())))

#방문 위치 표시
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1 # 현재 방문 리스트 처리

#북 동 남 서 방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽
def turnleft():
    global direction
    direction = ( direction -1 ) % 4

#시뮬레이션 시작
count = 1 # 첫 위치에 대한 표시
turn_time = 0 # 회전 횟수 ( 최대 4 번 )

while True:
    turnleft()
    nx = x + dx[direction]
    ny = y + dy[direction]

#방문하지 않고 육지인경우
    if visited[nx][ny] == 0 and mapp[nx][ny] == 0:
        visited[nx][ny] == 1
        count += 1
        turntime = 0 #이거 왜 함?
        continue #이거 왜 함 ?
    else:
        turn_time +=1
    
#4방향 다 안되는경우
    if turntime == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if mapp[nx][ny] == 0:
            x,y = nx, ny 

        else:
            break
        turntime = 0 #이건 if문 실행 되고 if문 또 실행되고 바로 여기로 점프되는거야 ?

print(count)

