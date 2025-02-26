# def solution(players, callings):
#     for i in range(len(players)):
#         if callings in players:
#             players[i-1] = players[i]
#             players[i] = players[i-1]
            
#     print(players)

#     for i in callings:
#         if i in players:
#             idx = players.index(i) #3,3,4,4
            
#             if idx > 0:
#                 players[idx], players[idx-1] = players[idx-1] , players[idx]
                
#     return players
        
    #인덱스 > 시간 초과 , enumerate사용하여 딕셔너리로
    
def solution(players, callings):
    playerdict = {player : idx for idx , player in enumerate(players)}
    
    for call in callings:
        idx = playerdict[call] #{'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
        
        players[idx] , players[idx-1] = players[idx-1] , players[idx]
        
        playerdict[players[idx]] = idx
        playerdict[players[idx-1]] = idx-1
        
    return players
    
