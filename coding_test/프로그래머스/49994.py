def solution(dirs): #dirs : 명령어 
    x, y = 0,0  # 초기위치 지정
    paths = [] # 중복된 값 저장 안한거 리스트

    move = { #UDRL 
        "U" : (0,1), #오른쪽
        "D" : (0 , -1), #왼쪽
        "R" : (1, 0), #오른쪽
        "L" : (-1 ,0) #왼쪽
    }

    for d in dirs:
        nx,ny = x + move[d][0] , y + move[d][1] #x좌표의 의미 , y좌표의 의미


        #-5 에서 5 넘지 않게 
        if -5 <= nx <= 5 and -5 <= ny <= 5: # 순방향 , 역뱡향
            path1 = (x,y, nx, ny)
            path2 = (nx , ny, x, y)

            if path1 not in paths and path2 not in paths:
                paths.append(path1) 

            x,y = nx, ny #캐릭터 이동

    return len(paths)
