# def solution(park, routes):
#     #먼저 S의 위치 찾기
#     a = {park[row][col] : (row, col) for row in range(len(park)) for col in range(len(park[row]))}
    
#     start = a["S"]
    
#     directions = {
#     "N": (-1, 0),  
#     "S": (1, 0),   
#     "W": (0, -1), 
#     "E": (0, 1)  
#     }
    
#     for i in routes:
#         dirr, distance = i.split()
#         distance = int(distance)
        
#         for j in park:
#             for k in j:
#                 if k == "O":
#                     newx = start[0] + (directions[dirr][0] * distance)
#                     newy = start[1] + (directions[dirr][0] * distance)
#                 elif k == "X":
#                     break
#     answer = []        
#     if 0 <= newx <= len(park) and 0 < newy <= len(park[0]):
#         answer.append(newx)
#         answer.append(newy)
    
#     return answer

def solution(park, routes):
    
    a = {park[row][col]: (row, col) for row in range(len(park)) for col in range(len(park[row])) if park[row][col] == "S"}
    start = a["S"]

  
    directions = {
        "N": (-1, 0), "S": (1, 0),
        "W": (0, -1), "E": (0, 1)
    }

  
    for i in routes:
        dirr, distance = i.split()
        distance = int(distance)

       
        newx, newy = start[0] + directions[dirr][0] * distance, start[1] + directions[dirr][1] * distance

        
        if 0 <= newx < len(park) and 0 <= newy < len(park[0]) and all(park[start[0] + directions[dirr][0] * step][start[1] + directions[dirr][1] * step] != "X" for step in range(1, distance + 1)):
            start = (newx, newy)  

    return list(start)  
