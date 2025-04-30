# N = int(input()) # 먼저 받음
# M = input().split()

# x , y = 1, 1

# # for i in range(1, N+1):
# #     for j in range(1, N+1):
# #         map = [i][j]

# dx = [ 0 , -1 , 0 , 1] # 동 서 남 북
# dy = [1, 0 , -1 , 0]
  
# for k in M:
#     if k == L:
#         nx = x + dx[1]

#     if k == R:#동
#         ny = y + dy[0]
    
#     if k == U: #위로 , 북
#         nx = x + dx[3]
        
#     if k == D:
#         ny = y + dy[2]

# if nx >= N or ny >= N:
#     continue

# print(map)

#상하좌우
N = int(input()) # 5
M = input().split() # L R U D D

x , y = 1,1

dx = [0 , 0 , -1 , 1] # L R U D
dy = [-1, 1 , 0 , 0]
move = ["L" , "R" ,"U" , "D"]

for k in M:
    for i in range(4):
        if k == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= N and 1 <= ny <= N:
                x , y = nx , ny 

print(x,y)