class chess:
    name="You're not suppossed to see this."
    def __init__(self,name): self.name=name
    color="You're not suppossed to see this."
    piece="You're not suppossed to see this."
    x=0
    y=0
    hasMoved=False
    alive=True
    extra=False
    tempcolor="You're not suppossed to see this."
    temppiece="You're not suppossed to see this."
    tempx=0
    tempy=0
    temphasMoved=False
    tempalive=True
    tempextra=False
    def reset(self,color,piece,x,y,extra=False):
        self.color=color
        self.piece=piece
        self.x=x
        self.y=y
        self.hasMoved=False
        self.alive=True
        self.extra=extra
        self.clone()
    def clone(piece): [piece.tempcolor,piece.temppiece,piece.tempx,piece.tempy,piece.tempalive,piece.temphasMoved,piece.tempextra]=[piece.color,piece.piece,piece.x,piece.y,piece.alive,piece.hasMoved,piece.extra]
    def declone(piece): [piece.color,piece.piece,piece.x,piece.y,piece.alive,piece.hasMoved,piece.extra]=[piece.tempcolor,piece.temppiece,piece.tempx,piece.tempy,piece.tempalive,piece.temphasMoved,piece.tempextra]
def intToAlphabet(x):
    alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    ret=""
    place=0
    y=0
    while y<x:
        place+=1
        y=0
        for w in range(place): y+=(26**(w+1))
    for i in range(place-1,0,-1):
        if x//(26**i)==27:
            ret+="Z"
            x=(x%(26**i))+26
        else:
            ret+=alpha[x//(26**i)-1]
            x%=26**i
    ret+=alpha[x-1]
    return ret
def alphabetToInt(y):
    alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    ret=0
    x=""
    for i in range(len(y)): x=y[i]+x
    for i in range(len(x)):
        ret+=(26**i)*(alpha.index(x[i])+1)
    return ret
def swap(swap,x,y):
    if swap==x: return y
    if swap==y: return x
def pos(piece,x,y): [piece.x,piece.y]=[x,y]
def colorrev(color,x):
    if color=="w": return x
    else: return -1*x
def check(xy):
    global allPieces
    ret="none"
    for piece in allPieces:
        if xy==[piece.x,piece.y] and piece.alive: ret=piece
    return ret
def kingcheck(color):
    global allPieces
    ret=False
    if color=="b":
        xy=[allPieces[31].x,allPieces[31].y]
        for piece in allPieces:
            if xy in move(piece): ret=True
    else:
        xy=[allPieces[15].x,allPieces[15].y]
        for piece in allPieces:
            if xy in move(piece): ret=True
    return ret
def moveto(x,y,color,canCapture=True,mustCapture=False):
    check=check([x,y])
    if (check=="none" and not mustCapture): return True
    elif not isinstance(check,str):
        if (check.color!=color and canCapture): return True 
    else: return False
def linearmoveto(possible,x,y,color,acrossx,acrossy,xlimit=False,ylimit=False,xdirec=0,ydirec=0,xmin=1,ymin=1,xmult=1,ymult=1,canJump=False,canCapture=True,mustCapture=False):
    global board
    if not isinstance(xlimit,bool):
        xplim=x+xlimit+1
        xnlim=x-xlimit-1
        if xplim>board[0]+1: xplim=board[0]+1
        if xnlim<0: xnlim=0
    else:
        xplim=board[0]+1
        xnlim=0
    if not isinstance(ylimit,bool):
        yplim=y+ylimit+1
        ynlim=y-ylimit-1
        if yplim>board[1]+1: yplim=board[1]+1
        if ynlim<0: ynlim=0
    else:
        yplim=board[1]+1
        ynlim=0
    xdirec=colorrev(color,xdirec)
    ydirec=colorrev(color,ydirec)
    if acrossx and not acrossy:
        if xdirec>=0:
            for i in range(x+xmult,xplim,xmult):
                if moveto(i,y,color,canCapture,mustCapture):
                    if i>=x+xmin: possible.append([i,y])
                elif not canJump: break
        if xdirec<=0:
            for i in range(x-xmult,xnlim,-1*xmult):
                if moveto(i,y,color,canCapture,mustCapture):
                    if i<=x-xmin: possible.append([i,y])
                elif not canJump: break
    if acrossy and not acrossx:
        if ydirec>=0:
            for i in range(y+ymult,yplim,ymult):
                if moveto(x,i,color,canCapture,mustCapture):
                    if i>=y+ymin: possible.append([x,i])
                elif not canJump: break
        if ydirec<=0:
            for i in range(y-ymult,ynlim,-1*ymult):
                if moveto(x,i,color,canCapture,mustCapture):
                    if i<=y-ymin: possible.append([x,i])
                elif not canJump: break
    if acrossx and acrossy:
        if ydirec>=0:
            if xdirec>=0:
                j=y+ymult
                for i in range(x+xmult,xplim,xmult):
                    if j>=yplim: break
                    if moveto(i,j,color,canCapture,mustCapture):
                        if i>=x+xmult and j>=y+ymin: possible.append([i,j])
                    elif not canJump: break
                    j+=ymult
            if xdirec<=0:
                j=y+ymult
                for i in range(x-xmult,xnlim,-1*xmult):
                    if j>=yplim: break
                    if moveto(i,j,color,canCapture,mustCapture):
                        if i<=x-xmin and j>=y+ymin: possible.append([i,j])
                    elif not canJump: break
                    j+=ymult
        if ydirec>=0:
            if xdirec>=0:
                j=y-ymult
                for i in range(x+xmult,xplim,xmult):
                    if j<=ynlim: break
                    if moveto(i,j,color,canCapture,mustCapture):
                        if i>=x+xmin and j<=y-ymin: possible.append([i,j])
                    elif not canJump: break
                    j-=-1*ymult
            if xdirec<=0:
                j=y-ymult
                for i in range(x-xmult,xnlim,-1*xmult):
                    if j<=ynlim: break
                    if moveto(i,j,color,canCapture,mustCapture):
                        if i<=x-xmin and j<=y-ymin: possible.append([i,j])
                    elif not canJump: break
                    j-=-1*ymult
    return possible
def checkcheck(piece,possible):
    global allPieces,board
    if possible==[]: possible="none"
    else:
        for pieces in allPieces: pieces.clone()
        for i in possible:
            if check(i)!="none": check(i).alive=False
            piece.x=i[0]
            piece.y=i[1]
            if kingcheck(piece.color): possible.remove(i)
            elif i[0]<1 or i[0]>board[0] or i[1]<1 or i[1]>board[1]: possible.remove(i)
        for pieces in allPieces: pieces.declone()
    return possible
def possiblePieces(color):
    global allPieces
    possible=["none"]
    if color=="w":
        for piece in allPieces:
            pieces=checkcheck(piece,move(piece))
            if piece.color=="w" and pieces!="none": possible.append(piece)
    else:
        for piece in allPieces:
            pieces=checkcheck(piece,move(piece))
            if piece.color=="b" and pieces!="none": possible.append(piece)
    if len(possible)>1:possible.remove("none")
    return possible
def translateMoveMade(moveMade):
    if isinstance(moveMade[0],int): moveMade=intToAlphabet(moveMade[0])+""+str(moveMade[1])
    else:
        for char in range(len(moveMade)):
            if moveMade[char].isdigit(): charindex=char
        moveMade=[alphabetToInt(moveMade[:charindex]),int(moveMade[charindex:])]
    return moveMade
def translatePossiblePieces(possiblePieces):
    ret=""
    for piece in range(len(possiblePieces)):
        ret+=possiblePieces[piece].piece+" "
        for char in possiblePieces[piece].name:
            if char.isdigit(): ret+=char
        ret+=", "
    return ret[:-2]
def display():
    global board
    print("┌───"+"┬───"*(board[0]-1)+"┐")
    for y in range(board[1],0,-1):
        for x in range(1,board[0]+1):
            print(end="│ ")
            piece=check([x,y])
            if piece!="none":
                if piece.alive:
                    if piece.color=="w": color="\033[33m"
                    else: color="\033[31m"
                    if piece.piece=="Pawn": name="p"
                    elif piece.piece=="Knight": name="k"
                    elif piece.piece=="Rook": name="R"
                    elif piece.piece=="Bishop": name="B"
                    elif piece.piece=="Queen": name="Q"
                    elif piece.piece=="King": name="K"
                    name=color+name
                else: name=" "
            else: name=" "
            print(name,end="\033[m")
            print(end=" ")
        print("│")
        if y!=1: print("├───"+"┼───"*(board[0]-1)+"┤")
        else: continue
    print("└───"+"┴───"*(board[0]-1)+"┘")
def move(piece):
    global board
    possible=[]
    if piece.alive:
        if piece.piece=="Pawn":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,0,1,ydirec=1,canCapture=False)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,1,1,ydirec=1,mustCapture=True)
            if not piece.hasMoved: possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,0,2,ydirec=1,ymin=2,canCapture=False)
        elif piece.piece=="Rook":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True))
        elif piece.piece=="Knight":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,2,1,xmult=2,canJump=True)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,1,2,ymult=2,canJump=True)
        elif piece.piece=="Bishop":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True)
        elif piece.piece=="Queen":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True)
        elif piece.piece=="King":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False,1,1)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,1,1)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,1,1)
    return possible
def reset():
    global allPieces
    allPieces[0].reset("w","Pawn",1,2)
    allPieces[1].reset("w","Pawn",2,2)
    allPieces[2].reset("w","Pawn",3,2)
    allPieces[3].reset("w","Pawn",4,2)
    allPieces[4].reset("w","Pawn",5,2)
    allPieces[5].reset("w","Pawn",6,2)
    allPieces[6].reset("w","Pawn",7,2)
    allPieces[7].reset("w","Pawn",8,2)
    allPieces[8].reset("w","Rook",1,1)
    allPieces[9].reset("w","Rook",8,1)
    allPieces[10].reset("w","Knight",2,1)
    allPieces[11].reset("w","Knight",7,1)
    allPieces[12].reset("w","Bishop",3,1)
    allPieces[13].reset("w","Bishop",6,1)
    allPieces[14].reset("w","Queen",4,1)
    allPieces[15].reset("w","King",5,1)
    allPieces[16].reset("b","Pawn",8,7)
    allPieces[17].reset("b","Pawn",7,7)
    allPieces[18].reset("b","Pawn",6,7)
    allPieces[19].reset("b","Pawn",5,7)
    allPieces[20].reset("b","Pawn",4,7)
    allPieces[21].reset("b","Pawn",3,7)
    allPieces[22].reset("b","Pawn",2,7)
    allPieces[23].reset("b","Pawn",1,7)
    allPieces[24].reset("b","Rook",8,8)
    allPieces[25].reset("b","Rook",1,8)
    allPieces[26].reset("b","Knight",7,8)
    allPieces[27].reset("b","Knight",2,8)
    allPieces[28].reset("b","Bishop",6,8)
    allPieces[29].reset("b","Bishop",3,8)
    allPieces[30].reset("b","Queen",4,8)
    allPieces[31].reset("b","King",5,8)
#┌───┬───┬───┬───┬───┬───┬───┬───┐
#│ R │ k │ B │ Q │ K │ B │ k │ R │
#├───┼───┼───┼───┼───┼───┼───┼───┤
#│ p │ p │ p │ p │ p │ p │ p │ p │
#├───┼───┼───┼───┼───┼───┼───┼───┤
#│   │   │   │   │   │   │   │   │
#├───┼───┼───┼───┼───┼───┼───┼───┤
#│   │   │   │   │   │   │   │   │
#├───┼───┼───┼───┼───┼───┼───┼───┤
#│   │   │   │   │   │   │   │   │
#├───┼───┼───┼───┼───┼───┼───┼───┤
#│   │   │   │   │   │   │   │   │
#├───┼───┼───┼───┼───┼───┼───┼───┤
#│ p │ p │ p │ p │ p │ p │ p │ p │
#├───┼───┼───┼───┼───┼───┼───┼───┤
#│ R │ k │ B │ Q │ K │ B │ k │ R │
#└───┴───┴───┴───┴───┴───┴───┴───┘
allPieces=[chess("wpawn1"),chess("wpawn2"),chess("wpawn3"),chess("wpawn4"),chess("wpawn5"),chess("wpawn6"),chess("wpawn7"),chess("wpawn8"),chess("wrook1"),chess("wrook2"),chess("wknight1"),chess("wknight2"),chess("wbishop1"),chess("wbishop2"),chess("wqueen1"),chess("wking1"),chess("bpawn1"),chess("bpawn2"),chess("bpawn3"),chess("bpawn4"),chess("bpawn5"),chess("bpawn6"),chess("bpawn7"),chess("bpawn8"),chess("brook1"),chess("brook2"),chess("bknight1"),chess("bknight2"),chess("bbishop1"),chess("bbishop2"),chess("bqueen1"),chess("bking1")]
board=[8,8]
play="y"
while play=="y" or play=="Y":
    color="w"
    reset()
    while True:
        display()
        if possiblePieces(color)==["none"]:
            if kingcheck(color): print("The",color,"player is in checkmate!")
            else: print("Stalemate!")
            print("The",swap(color,"w","b"),"player wins!")
            break
        print("Player",color,"can move the following pieces:",translatePossiblePieces(possiblePieces(color)))
        while True:
            pieceMoveMade=color+input("What piece do you want to move? ").strip(" ").lower()
            for piece in allPieces:
                if pieceMoveMade==piece.name: pieceMoveMade=piece
            if pieceMoveMade!="none":
                if pieceMoveMade in possiblePieces(color): break
                else: print("You can't move that piece!")
            else: print("That is not a valid piece!")
        while True:
            pieceMoveMadeMoves=move(pieceMoveMade)
            moveMade=translateMoveMade(input("Where do you want to move "+translatePossiblePieces([pieceMoveMade])+"? "+str(checkcheck(pieceMoveMade,pieceMoveMadeMoves))+" "))
            if moveMade not in pieceMoveMadeMoves:
                print("That's not a vlaid move!")
                continue
            elif moveMade not in checkcheck(pieceMoveMade,pieceMoveMadeMoves):
                print("That would put your king in check!")
                continue
            else: 
                print(translatePossiblePieces([pieceMoveMade]),"moved to",translateMoveMade(moveMade))
                break
        if pieceMoveMade.piece=="King": pieceMoveMade.tempx=pieceMoveMade.x
        if check(moveMade)!="none": check(moveMade).alive=False
        [pieceMoveMade.x,pieceMoveMade.y]=moveMade
        if pieceMoveMade.piece=="Pawn":
            if moveMade[1]==board[0]+(colorrev(pieceMoveMade.color,(board[0]-1)/2)-1*((board[0]-1)/2)): pieceMoveMade.piece=input("What do you wan to promote your pawn to?")
            if not pieceMoveMade.hasMoved: pieceMoveMade.extra=True
            else: pieceMoveMade.extra=False
        pieceMoveMade.hasMoved=True
        color=swap(color,"w","b")
        if kingcheck(color): print("The",color,"player is in check.")
    play=input("Do you want to play again? (Y/N) ")
print("Goodbye!")
