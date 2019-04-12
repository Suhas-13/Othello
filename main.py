
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
    output=('','')
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
       val1=(letterlist.index(s[0].lower()))
    elif s[1].isalpha():
        val1=(letterlist.index(s[1].lower()))

    if s[0].isnumeric():
        val0=numberlist.index(str(s[0]))
    elif s[1].isnumeric():
        val0=numberlist.index(str(s[1]))
    return(val0,val1)
def indexToStr(t):
    letterlist=['a','b','c','d','e','f','g','h']
    numberlist=[1,2,3,4,5,6,7,8]
    return(letterlist[t[1]] + str(numberlist[t[0]]))
        
       
def loadGame():
    
    try:
        with open("game.txt") as f:
            file = f.read().splitlines() 

    except:
        raise FileNotFoundError
    
    try:
        game={'player1':file[0],
              'player2':file[1],
              'who':file[2],
              'game':[]
               }
        file.pop(0)
        file.pop(0)
        file.pop(0)
        for i in file:
            game['game'].append(i.split(","))
    except:
        raise ValueError
    return(game)
def getLine(board,who,pos,dirs):
    #Couldn't use dir as it is a keyword so using dirs instead
    if who == 1:
        whonot=2
    elif who == 2:
        whonot=1
    output=[]

    val=[]
    

    if dirs[0] == 0:
        addone=0
    elif dirs[0]==1:
        addone=1
    elif dirs[0]==-1:
        addone=-1
    if dirs[1]==0:
        addtwo=0
    elif dirs[1]==1:
        addtwo=1
    elif dirs[1]==-1:
        addtwo=-1
    countone=addone
    counttwo=addtwo
    try:
        flag=True
        for i in range(0,8):
            val=[pos[0]+countone,pos[1]+counttwo]
            if ( int(board[val[0]][val[1]])) == who:
                break
            elif ( int(board[val[0]][val[1]])) == whonot:
                output.append(val)
            elif ( int(board[val[0]][val[1]])) == 0:
                output=[]
                break
            countone+=addone
            counttwo+=addtwo

            if val[0] ==0 or val[1] ==0:
                break
        
        return(output)
    except:
        pass
        
def getValidMoves(board,who):
    output=[]
    for r in range(0,7):
        for c in range(0,7):
            if int(board[r][c])==0:
                line1=getLine(board,who,(r,c),(0,1))
                if len(line1)>0:
                    output.append((r,c))
                    
                line2=getLine(board,who,(r,c),(1,0))
                if len(line2)>0:
                    output.append((r,c))

                line3=getLine(board,who,(r,c),(1,1))
                if len(line3)>0:
                    output.append((r,c))
                
                line4=getLine(board,who,(r,c),(0,-1))
                if len(line4)>0:
                    output.append((r,c))
                
                line5=getLine(board,who,(r,c),(-1,0))
                if len(line5)>0:
                    output.append((r,c))
                    
                line6=getLine(board,who,(r,c),(-1,-1))
                if len(line6)>0:
                    output.append((r,c))
                    
                line7=getLine(board,who,(r,c),(-1,1))
                if len(line7)>0:
                    output.append((r,c))
                    
                line8=getLine(board,who,(r,c),(1,-1))
                if len(line8)>0:
                    output.append((r,c))

               
    return(list(set(output)))
