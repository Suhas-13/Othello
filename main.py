
from copy import deepcopy
"""
game={
    'player1':p1,
    'player2':p2,
    'who':1,
    'board':
[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0,0, 2, 1, 0, 0, 0],
[0, 0, 0, 1, 2, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
}
"""
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
    
    
    mapboard=deepcopy(board)
    maincount=0
    for lists in mapboard:
        listcount=0
        for i in lists:
            
            if int(i) == 1:
                mapboard[maincount][listcount]="X"
            elif int(i) ==2:
                mapboard[maincount][listcount]="O"
            elif int(i) == 0:
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
              'who':int(file[2]),
              'board':[]
               }
        file.pop(0)
        file.pop(0)
        file.pop(0)
        for i in file:
            game['board'].append(i.split(","))
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
def makeMove(board,move,who):
    r=move[0]
    c=move[1]
    output=[]
    board5=board
    board5[move[0]][move[1]] = who
    line1=getLine(board5,who,(r,c),(0,1))
    if len(line1)>0:
        for i in line1:
            output.append(i)
        
    line2=getLine(board5,who,(r,c),(1,0))
    if len(line2)>0:
        for i in line2:
            output.append(i)

    line3=getLine(board5,who,(r,c),(1,1))
    if len(line3)>0:
        for i in line3:
            output.append(i)
    
    line4=getLine(board5,who,(r,c),(0,-1))
    if len(line4)>0:
        for i in line4:
            output.append(i)
    
    line5=getLine(board5,who,(r,c),(-1,0))
    if len(line5)>0:
        for i in line5:
            output.append(i)
        
    line6=getLine(board5,who,(r,c),(-1,-1))
    if len(line6)>0:
        for i in line6:
            output.append(i)
        
    line7=getLine(board5,who,(r,c),(-1,1))
    if len(line7)>0:
        for i in line7:
            output.append(i)
        
    line8=getLine(board5,who,(r,c),(1,-1))
    if len(line8)>0:
        for i in line8:
            output.append(i)

    for i in output:
        board[i[0]][i[1]]=(who)
    return(board5)
def scoreBoard(board):
    player1=0
    player2=0
    for r in range(0,7):
        for c in range(0,7):
            if int(board[r][c]) == 1:
                player1+=1
            elif int(board[r][c])==2:
                player2+=1
    return(player1-player2)
def suggestMove1(board,who):
    moves=getValidMoves(board,who)
    
    highest=0
    highestmove=()
    for move in moves:
        board2=deepcopy(board)
        count=scoreBoard(makeMove(board2,move,who))
        if  count> highest:
            highest=count
            highestmove=move
    if highest ==0:
        highestmove=moves[0]
    return(highestmove)
def play():
    print("Welcome to Othello")
    print("\n\nEnter player name's or c for computer and l for load")
    p1=''
    p2=''
    while p1 == '': 
        p1=input("Please enter player #1's name: ")
    if p1.lower() == 'l':
        game=loadGame()
    else:
        while p2 == '':
            p2=input("Please enter player #2's name: ")
            print("\n\nLet's begin!\n\n")
            p1=p1.capitalize()
            p2=p2.capitalize()
            game={
            'player1':p1,
            'player2':p2,
            'who':1,
            'board':
        [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0,0, 2, 1, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]
        }
    endcount=0
    flag=True
    players=[str(game['player1']),str(game['player2'])]
    printBoard(game['board'])
    while flag==True:
        
        if players[game['who']-1].lower() == 'c':
            if len(getValidMoves(game['board'],game['who'])) > 0:
                
                endcount=0
                game['board']=makeMove(game['board'],suggestMove1(game['board'],game['who']),game['who'])
                if game['who'] ==1:
                    game['who']=2
                elif game['who'] ==2:
                    game['who']=1
                print("\n\n")
                print("Computer has made it's move!")
                print("\n\n")
                printBoard(game['board'])
            else:
                endcount+=1
                print("No valid moves for Computer, skipping")
                if game['who']==1:
                    game['who']=2
                elif game['who']==2:
                    game['who']=1
                if endcount ==2:
                    print("\n\nGame Over\n\n")
                    if scoreBoard(game['board']) > 0:
                        print(players[0] + " has won with a score of " + str(scoreBoard(game['board'])))
                    elif scoreBoard(game['board']) < 0:
                        print(players[1] + " has won with a score of " + str(scoreBoard(game['board'])/-1))
                    else:
                        print("\n\nThe game has ended in a tie\n\n")
                    break
                
                
            
        else:   
            if game['who'] == 1:
                if len(getValidMoves(game['board'],game['who'])) > 0:
                    endcount=0
                    move=input("\n\nPlease enter a move P1: ")
                    move=strToIndex(move)
                    if move not in (getValidMoves(game['board'],game['who'])):
                        pass
                    elif move == None:
                        pass
                    else:
                        game['board']=makeMove(game['board'],move,game['who'])
                        game['who']=2
                        printBoard(game['board'])
        
                else:
                    print("No valid moves for Player#1, skipping")
                    endcount+=1
                    game['who']=2
                    if endcount ==2:
                        print("Game Over, no more valid moves!")
                        if scoreBoard(game['board']) > 0:
                            print(players[0] + " has won with a score of " + str(scoreBoard(game['board'])))
                        elif scoreBoard(game['board']) < 0:
                            print(players[1] + " has won with a score of " + str(scoreBoard(game['board'])/-1))
                        else:
                            print("The game has ended in a tie")
                        break
                        
                    
                
            elif game['who'] == 2:
                
                if len(getValidMoves(game['board'],game['who'])) > 0:
                    endcount=0
                    move=input("\n\nPlease enter a move P2: ")
                    move=strToIndex(move)
                    if move not in (getValidMoves(game['board'],game['who'])):
                        pass
                    elif move == None:
                        pass
                    else:
                        game['board']=makeMove(game['board'],move,game['who'])
                        game['who']=1
                        printBoard(game['board'])                
        
                else:
                    print("No valid moves for Player #2")
                    endcount+=1
                    game['who']=1
                    if endcount ==2:
                        print("\n\nGame Over, no more valid moves!")
                        if scoreBoard(game['board']) > 0:
                            print(players[0] + " has won with a score of " + str(scoreBoard(game['board'])))
                        elif scoreBoard(game['board']) < 0:
                            print(players[1] + " has won with a score of " + str(scoreBoard(game['board'])/-1))
                        else:
                            print("\n\nThe game has ended in a tie")
                        break
                        
                        
                        
                        
