
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
def strToIndex(s):
    letterlist=['a','b','c','d','e','f','g','h']
    output=['','']
    numberlist=['1','2','3','4','5','6','7','8']
    s=s.replace(" ","")
    if len(s) > 2:
        raise ValueError
    if len(s)<2:
        raise ValueError
    if s[0].isnumeric():
        if int(s[0]) not in [1,2,3,4,5,6,7,8]:
            raise ValueError
    elif s[1].isnumeric():
        if int(s[1]) not in [1,2,3,4,5,6,7,8]:
            raise ValueError
    else:
        raise ValueError
    if s[0].isalpha():
        if s[0].lower() not in ['a','b','c','d','e','f','g','h']:
            raise ValueError
    elif s[1].isalpha():
        
        if s[1].lower() not in ['a','b','c','d','e','f','g','h']:
            raise ValueError
    else:
        raise ValueError
    
    if s[0].isalpha():
       output[1]=(letterlist.index(s[0].lower()))
    elif s[1].isalpha():
        output[1]=(letterlist.index(s[1].lower()))

    if s[0].isnumeric():
        output[0]=numberlist.index(str(s[0]))
    elif s[1].isnumeric():
        output[0]=numberlist.index(str(s[1]))
    return(output)
        
       
