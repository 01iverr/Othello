def printer(board):
    # prints board on screen
    print("    A   B   C   D   E   F   G   H")
    for i in range(1,N+1):
        print(" ", "-"*33)
        print(i,"",end="|")
        for j in range(0,N):
            if (board[i-1][j] == 0):
                print("","X","", end="|")    
            elif (board[i-1][j] == 1):
                print("","O","",end="|")
            else :
                print(""," ","",end="|")
        print()
    print(" ","-"*33)


def dyskolia(): # gets depth for MiniMax algorithm
    while (True):
        try:
            d = int(input("Give the maximum search depth of MiniMax algorithm(>0): "))
            if (d>0):
                break
        except ValueError:
            print ("That was not a valid number.")
    return d


def seira():
    # dialegei o paixths an thelei na paiksei prwtos
    while (True):
        answer = input("\nWould you like to play first?\nPress y for Yes οr n for No: ")
        if (answer.upper() != "Y" and answer.upper() != "N"):
            print("Invalid option.")
            continue
        break
    if (answer.upper()=="Y"):
        return 0    # mayra pionia einai to 0 (X)
    elif (answer.upper()=="N"):
        return 1    # aspra pionia einai to 1 (O)

def checkIfCanPlay(board, xrwma):
    # check if player defined by xrvma can play
    # board:    current board
    # xrvma:    player to play currently (0 h 1 dhl. X h O)
    for i in range(N):
        for j in range(N):
            if (validPlaceOne(board,i,j,xrwma)):
                return True
    return False

def hasFilled(board):
    # whether board has been filled
    for i in range(N):
        for j in range (N):
            if (board[i][j]==None):
                return False
    return True


def hasEnded(board):
    if (hasFilled(board)):
        return True
    if (not checkIfCanPlay(board, 0) and not checkIfCanPlay(board, 1)):
        return True


def validPlaceOne(board, i, j, xrvma):   # elegxei an h thesi einai apodekth
    # board: current board
    # i,j:   coordinates of place in board
    # xrvma: player to play currently
    # arxika ginetai elegxos an yparxei pouli gyrw apo th thesi
    # kai meta kaleitai h validPlaceTwo

    f = False
    
    if (j+1<N):
        if (board[i][j+1] != None):
            f=True
        if (i+1<N):
            if (board[i+1][j+1] != None):
                f=True
        if (i-1>=0):
            if (board[i-1][j+1] != None):
                f=True
			
    if (j-1>=0):
        if (board[i][j-1] != None):
            f=True
        if (i+1<N):
            if (board[i+1][j-1] != None):
                f=True
        if (i-1<N):
            if (board[i-1][j-1] != None):
                f=True
    if (i+1<N):
        if (board[i+1][j] != None):
            f=True
    if (i-1>=0):
        if (board[i-1][j] != None):
            f=True

    if(board[i][j] != None): 
        f = False
	
    if (f):
        return validPlaceTwo(board, i, j, xrvma)       


def validPlaceTwo(board, i, j, xrvma):
    # i,j:   coordinates of place in board
    # turn:  player to play currently
    # elegxos an yparxei epithesi apo auth th thesi se pouli tou antipalou

    # a killer is found when there's been attacks to opponent poulia and 
    # then one of it's own is found -> attack valid, killers+=1
    killers = 0     
    attcells = []   # attacked cells

    x, y = i+1, j+1
    attack = 0
    killers = 0
    while x < N and y < N: # diagwnia pros ta katv dejia
        if(board[x][y]!=xrvma and board[x][y]!=None):
            attack += 1
            attcells.append((x,y))
        if(board[x][y]==xrvma  and attack!=0):
            killers += 1
            break
        if (killers == 0 and not(board[x][y]!=xrvma and board[x][y]!=None)):
            for a in range(attack):
                attcells.pop()
            attack=0
            break
        if (board[x][y] == xrvma and attack == 0):
            break
        x += 1
        y += 1
    if (killers == 0):
        for a in range(attack):
            attcells.pop()
    
    x, y = i-1, j-1
    attack = 0
    killers = 0
    while x >= 0 and y >= 0: # diagwnia pros ta panw aristera
        if(board[x][y]!=xrvma and board[x][y]!=None):
            attack += 1
            attcells.append((x,y))
        if(board[x][y]==xrvma  and attack!=0):
            killers += 1
            break
        if (killers == 0 and not(board[x][y]!=xrvma and board[x][y]!=None)):
            for a in range(attack):
                attcells.pop()
            attack=0
            break
        if (board[x][y] == xrvma and attack == 0):
            break
        x -= 1
        y -= 1
    if (killers == 0):
        for a in range(attack):
            attcells.pop()
    
    x, y = i-1, j+1
    attack = 0
    killers = 0
    while x >= 0 and y < N:  # diagwnia pros ta panw dejia
        if(board[x][y]!=xrvma and board[x][y]!=None):
            attack += 1
            attcells.append((x,y))
        if(board[x][y]==xrvma  and attack!=0):
            killers += 1
            break
        if (killers == 0 and not(board[x][y]!=xrvma and board[x][y]!=None)):
            for a in range(attack):
                attcells.pop()
            attack=0
            break
        if (board[x][y] == xrvma and attack == 0):
            break
        x -= 1
        y += 1

    if (killers == 0):
        for a in range(attack):
            attcells.pop()
    
    x, y = i+1, j-1
    attack = 0
    killers = 0
    while x < N and y >= 0: # diagwnia prow ta katw aristera
        if(board[x][y]!=xrvma and board[x][y]!=None):
            attack += 1
            attcells.append((x,y))
        if(board[x][y]==xrvma  and attack!=0):
            killers += 1
            break
        if (killers == 0 and not(board[x][y]!=xrvma and board[x][y]!=None)):
            for a in range(attack):
                attcells.pop()
            attack=0
            break
        if (board[x][y] == xrvma and attack == 0):
            break
        x += 1
        y -= 1
    if (killers == 0):
        for a in range(attack):
            attcells.pop()
    
    x, y = i, j+1
    attack = 0
    killers = 0
    while y < N: # idia seira orizontia dejia
        if(board[x][y]!=xrvma and board[x][y]!=None):
            attack += 1
            attcells.append((x,y))
        if(board[x][y]==xrvma  and attack !=0):
            killers += 1
            break
        if (killers == 0 and not(board[x][y]!=xrvma and board[x][y]!=None)):
            for a in range(attack):
                attcells.pop()
            attack=0
            break
        if (board[x][y] == xrvma and attack == 0):
            break
        y += 1
    if (killers == 0):
        for a in range(attack):
            attcells.pop()
    
    x, y = i, j-1
    attack = 0
    killers = 0
    while y >= 0: # idia seira orizontia aristera
        if(board[x][y]!=xrvma and board[x][y]!=None):
            attack += 1
            attcells.append((x,y))
        if(board[x][y]==xrvma  and attack !=0):
            killers += 1
            break
        if (killers == 0 and not(board[x][y]!=xrvma and board[x][y]!=None)):
            for a in range(attack):
                attcells.pop()
            attack=0
            break
        if (board[x][y] == xrvma and attack == 0):
            break
        y -= 1
    if (killers == 0):
        for a in range(attack):
            attcells.pop()
    
    x, y = i-1, j
    attack = 0
    killers = 0
    while x >= 0: # idia sthlh katheta panw
       if(board[x][y]!=xrvma and board[x][y]!=None):
            attack += 1
            attcells.append((x,y))
       if(board[x][y]==xrvma  and attack !=0):
            killers += 1
            break
       if (killers == 0 and not(board[x][y]!=xrvma and board[x][y]!=None)):
           for a in range(attack):
               attcells.pop()
           attack=0
           break
       if (board[x][y] == xrvma and attack == 0):
           break
       x -= 1
    if (killers == 0):
        for a in range(attack):
            attcells.pop()

    x, y = i+1, j
    attack = 0
    killers = 0
    while x < N: # idia sthlh katheta katw
        if(board[x][y]!=xrvma and board[x][y]!=None):
            attack += 1
            attcells.append((x,y))
        if(board[x][y]==xrvma  and attack!=0):
            killers += 1
            break
        if (killers == 0 and not(board[x][y]!=xrvma and board[x][y]!=None)):
            for a in range(attack):
                attcells.pop()
            attack=0
            break
        if (board[x][y] == xrvma and attack == 0):
            break
        x += 1
    if (killers == 0):
        for a in range(attack):
            attcells.pop()
    
    if (len(attcells)==0):
        return None
    
    return attcells


def isOnBoard(x, y):
    # whether coordinates are on board
    return x >= 0 and x < N and y >= 0 and y < N


def getPlayerMove(board): 
    while (True):
        print("\nPlease enter the coordinates (ex. a3) of the cell you wish to place your piece: ", end = "")
        pmove = input().lower()

        if (len(pmove) != 2):
            print("Invalid input. \nMust enter two charcters: coloumn character (A-H) and row number (1-8) of cell. \nTry again.")
            continue

        if ((not pmove[0].isdigit()) and pmove[1].isdigit()):   #char number format
            pcol = ord(pmove[0]) - 97   # in ascii, 'a' = 97
            prow = int(pmove[1]) - 1    # numbers on board start from 1
        elif (pmove[0].isdigit() and (not pmove[1].isdigit())): #number char format
            prow = ord(pmove[1]) - 97   # in ascii, 'a' = 97
            pcol = int(pmove[0]) - 1    # numbers on board start from 1
        else:
            print("Invalid input. \nMust enter coloumn character (A-H) and row number (1-8) of cell. \nTry again.")
            continue

        if (not isOnBoard(prow, pcol)): #coordinates must be within board bounds
            print("Invalid input. \nMust enter coloumn character (A-H) and row number (1-8) of cell. \nTry again.")
            continue
        
        vPl = validPlaceOne(board, prow, pcol, s)
        if (vPl == None): 
            print("Invalid input. \nNot a valid move. Try again.")
            continue
        
        for c in vPl: # change symbol of attacked cells
            board[c[0]][c[1]] = s
        break

    return (prow, pcol)


def getChildren(board, xrwma):
    children = []
    for i in range(N):
        for j in range(N):
            isValid = validPlaceOne(board, i, j, xrwma)
            if (isValid != None):
                child = ([[board[i][j] for i in range(N)] for j in range(N)],(i,j), len(isValid)) #saves board and last move, and value of last move
                for c in isValid:
                    child[0][c[0]][c[1]] = xrwma
                child[0][i][j] = xrwma
                children.append(child)
    return children

def miniMax(board, turn, xrvma):
    if (xrvma == turn):
        return max((board,(None,None),None), 0, xrvma, (None,None,-10000000))
    return min((board,(None,None),None), 0, xrvma, (None,None,10000000))

def max(tuplee, depth, xrvma, chosen):
    # tuplee:   board, (i,j), val
    # depth:    current depth
    # xrvma:    who's playing (0 h 1, dhl. X h O antistoixa)
    # chosen:   position and value of max position

    board = tuplee[0]
    if (hasEnded(board) or depth == d):
        return chosen
    children = getChildren(board, xrvma)

    mrow = chosen[0] #grammh
    mcol = chosen[1] #sthlh 
    mval = chosen[2] #kerdos

    for c in children: #oles oi dynates kinhseis tou antipalou 
        (row,col,val) = min(c, depth+1, not xrvma, chosen) #ti 8a paiksei o antipalos g to sygkekrimeno paidi
        if (val >= mval):
            if (val == mval): #authaireta epilegoume na allazei
                    mrow = c[1][0]
                    mcol = c[1][1]
                    mval = c[2]
            else:
                mrow = c[1][0]
                mcol = c[1][1]
                mval = c[2]
    return (mrow, mcol, mval)

def min(tuplee, depth, xrvma, chosen): 
    # tuplee:   board, (i,j), val
    # depth:    current depth
    # xrvma:    who's playing (0 h 1, dhl. X h O antistoixa)
    # chosen:   position and value of min position

    board = tuplee[0]
    if (hasEnded(board) or depth == d):
        return chosen
    children = getChildren(board, xrvma)
    
    mrow = chosen[0]
    mcol = chosen[1]
    mval = chosen[2]

    for c in children:
        (row,col,val) = max(c, depth+1, not xrvma, chosen)
        if (val <= mval):
            if (val == mval): #authaireta epilegoume na allazei
                    mrow = c[1][0]
                    mcol = c[1][1]
                    mval = c[2]
            else:
                mrow = c[1][0]
                mcol = c[1][1]
                mval = c[2]
    return (mrow, mcol, mval)


def getScore(board):
    # calculate score
    xscore = 0
    oscore = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                xscore += 1
            if board[i][j] == 1:
                oscore += 1
    return (xscore, oscore)


def printScore(board): 
    print("The final score is......")
    fscore = getScore(board)

    print("Player score: ",fscore[s], "\nComputer score: ",fscore[(1 if s==0 else 0)])
    print(("Player" if fscore[s]>fscore[(1 if s==0 else 0)] else "Computer"), " wins!")
   
    print("\N{trophy}"*20)
    return


def playAgain():
    while (True):
        answer = input("\nDo you want to play again? \nPress y for Yes οr n for No: ")
        if (answer.upper() !="Y" and answer.upper()!="N"):
            print("Invalid option.")
            continue
        break
    print()
    if (answer.upper()=="Y"):
        play()
        playAgain()
    elif (answer.upper()=="N"):
        print ("The game will be terminated.")
        exit()


def play():
    global N
    N = 8
    board = [[None for i in range(N)] for j in range(N)] 
    global d
    d = dyskolia() #depth
    global metrhths
    global s 
    s = seira() #0: prwtos, 1:deuteros


    if (s == 1): #if player choose to play first
        metrhths = 0    #0: computer 1: paikths
    else:
        metrhths = 1

    board[3][3] = 1 # aspra pionia einai to 1 (O)
    board[3][4] = 0 # mayra pionia einai to 0 (X)
    board[4][3] = 0
    board[4][4] = 1
    
    while(True):
        print()
        printer(board)
        if (metrhths == 0): #computer plays
            print("It's the computer's turn (",("O" if s==0 else "X"),").")
            if (checkIfCanPlay(board,(1 if s==0 else 0))):
                moveComp = miniMax(board, metrhths, (1 if s==0 else 0))
                print("\n Computer move: (",chr(moveComp[1]+97),",",moveComp[0]+1,")") 
                vCom = validPlaceOne(board,moveComp[0],moveComp[1],(1 if s==0 else 0))
                if (vCom != None): #an brhke egkyrh 8esh o ypologisths paizei 
                    board[moveComp[0]][moveComp[1]] = (1 if s==0 else 0)
                    for c in vCom:
                        board[c[0]][c[1]] = (1 if s==0 else 0)
            else:
                print("No available moves for computer.")
            metrhths += 1
        else: # metrhths == 1 player plays
            print("It's the player's turn (",("X" if s==0 else "O"),").")
            if (checkIfCanPlay(board,s)):
                movePl = getPlayerMove(board)
                board[movePl[0]][movePl[1]] = s
            else:
                print("No available moves for player.")
            metrhths -= 1
        
        print()
        if(hasEnded(board)):
            break

    printer(board)
    printScore(board)
    playAgain()
    return

#GAME START
play()


