
from copy import deepcopy
game={
    'player1':'A',
    'player2':'C',
    'who':1,
    'board':
[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 2, 1, 0, 0, 0],
[0, 0, 1, 2, 2, 2, 0, 0],
[0, 0, 1, 2, 1, 0, 0, 0],
[0, 0, 0, 2, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
}
def newGame(player1,player2):
    
    if player1 == '':
        print("Please enter both names")
    elif player2=='':
        print("Please enter both names")
    game={
    'player1':player1,
    'player2':player2,
    'who':1,
    'board':
[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 2, 1, 0, 0, 0],
[0, 0, 0, 1, 2, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
}
    return(game)

def printBoard(board):
    #print(" ", end='')
    #for i in ['a','b','c','d','e','f','g']:
        #print("|"+i, end='')
    #print("|h|")
    #print(" +-+-+-+-+-+-+-+-+")
    mapboard=board
    maincount=0
    for lists in mapboard:
        listcount=0
        for i in lists:
            
            if i == 1:
                mapboard[maincount][listcount]="X"
            elif i ==2:
                mapboard[maincount][listcount]="O"
            elif i == 0:
                mapboard[maincount][listcount]=" "
            listcount+=1
        maincount+=1
    rep='  |a|b|c|d|e|f|g|h| \n  +-+-+-+-+-+-+-+-+ \n1 '+"|" + "|".join(mapboard[0]) +"|"+'\n2 '+"|" + "|".join(mapboard[1]) +"|" +'\n3 '+"|" + "|".join(mapboard[2]) +"|" '\n4 '+"|" + "|".join(mapboard[3]) +"|" '\n5 '+"|" + "|".join(mapboard[4]) +"|" '\n6 '+"|" + "|".join(mapboard[5]) +"|" '\n7 '+"|" + "|".join(mapboard[6]) +"|" '\n8 '+"|" + "|".join(mapboard[7]) +"|"+"\n  +-+-+-+-+-+-+-+-+" 
    print(rep)
def strToIndex(s)

   
