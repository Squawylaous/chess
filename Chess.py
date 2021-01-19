class chess:
    name="You're not suppossed to see this."
    color="You're not suppossed to see this."
    piece="You're not suppossed to see this."
    x=0
    y=0
    hasMoved=False
    alive=True
    extra=False
    displayName="You're not suppossed to see this."
    tempcolor="You're not suppossed to see this."
    temppiece="You're not suppossed to see this."
    tempx=0
    tempy=0
    temphasMoved=False
    tempalive=True
    tempextra=False
    tempdisplayName="You're not suppossed to see this."
    def reset(self,color,piece,displayName,x,y,alive=True,hasMoved=False,extra=False):
        self.color=color
        self.piece=piece
        self.x=x
        self.y=y
        self.hasMoved=hasMoved
        self.alive=alive
        self.extra=extra
        self.displayName=displayName
        num=0
        for pieces in allPieces:
            if allPieces.piece==piece: num+=1
        self.name=color+piece.lower()+str(num)
        self.clone()
    def clone(piece): [piece.tempcolor,piece.temppiece,piece.tempx,piece.tempy,piece.tempalive,piece.temphasMoved,piece.tempextra,piece.tempdisplayName]=[piece.color,piece.piece,piece.x,piece.y,piece.alive,piece.hasMoved,piece.extra,piece.displayName]
    def declone(piece): [piece.color,piece.piece,piece.x,piece.y,piece.alive,piece.hasMoved,piece.extra,piece.displayName]=[piece.tempcolor,piece.temppiece,piece.tempx,piece.tempy,piece.tempalive,piece.temphasMoved,piece.tempextra,piece.tempdisplayName]
def fill(x,y): return str(x)+(" "*(y-len(str(x))))
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
    else: return -x
def check(xy):
    global allPieces
    ret="none"
    for piece in allPieces:
        if xy==[piece.x,piece.y] and piece.alive: ret=piece
    return ret
def kingcheck(color):
    global allPieces
    ret=False
    kings=[]
    for piece in allPieces:
        if piece.piece=="King" and piece.color=color: kings.append(piece)
    for king in kings:
        for piece in allPieces:
            if piece.piece=="King": break
            elif [king.x,king.y] in move(piece): ret=True
    return ret
def moveto(x,y,color,canCapture=True,mustCapture=False):
    piece=check([x,y])
    if (piece=="none" and not mustCapture): return True
    elif not isinstance(piece,str):
        if (piece.color!=color and canCapture): return True 
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
                    if check([i,y])!="none":
                        if not canJump: break
                elif not canJump: break
        if xdirec<=0:
            for i in range(x-xmult,xnlim,-xmult):
                if moveto(i,y,color,canCapture,mustCapture):
                    if i<=x-xmin: possible.append([i,y])
                    if check([i,y])!="none":
                        if not canJump: break
                elif not canJump: break
    if acrossy and not acrossx:
        if ydirec>=0:
            for i in range(y+ymult,yplim,ymult):
                if moveto(x,i,color,canCapture,mustCapture):
                    if i>=y+ymin: possible.append([x,i])
                    if check([x,i])!="none":
                        if not canJump: break
                elif not canJump: break
        if ydirec<=0:
            for i in range(y-ymult,ynlim,-ymult):
                if moveto(x,i,color,canCapture,mustCapture):
                    if i<=y-ymin: possible.append([x,i])
                    if check([x,i])!="none":
                        if not canJump: break
                elif not canJump: break
    if acrossx and acrossy:
        if ydirec>=0:
            if xdirec>=0:
                j=y+ymult
                for i in range(x+xmult,xplim,xmult):
                    if j>=yplim: break
                    if moveto(i,j,color,canCapture,mustCapture):
                        if i>=x+xmult and j>=y+ymin: possible.append([i,j])
                        if check([i,j])!="none":
                            if not canJump: break
                    elif not canJump: break
                    j+=ymult
            if xdirec<=0:
                j=y+ymult
                for i in range(x-xmult,xnlim,-xmult):
                    if j>=yplim: break
                    if moveto(i,j,color,canCapture,mustCapture):
                        if i<=x-xmin and j>=y+ymin: possible.append([i,j])
                        if check([i,j])!="none":
                            if not canJump: break
                    elif not canJump: break
                    j+=ymult
        if ydirec>=0:
            if xdirec>=0:
                j=y-ymult
                for i in range(x+xmult,xplim,xmult):
                    if j<=ynlim: break
                    if moveto(i,j,color,canCapture,mustCapture):
                        if i>=x+xmin and j<=y-ymin: possible.append([i,j])
                        if check([i,j])!="none":
                            if not canJump: break
                    elif not canJump: break
                    j-=ymult
            if xdirec<=0:
                j=y-ymult
                for i in range(x-xmult,xnlim,-xmult):
                    if j<=ynlim: break
                    if moveto(i,j,color,canCapture,mustCapture):
                        if i<=x-xmin and j<=y-ymin: possible.append([i,j])
                        if check([i,j])!="none":
                            if not canJump: break
                    elif not canJump: break
                    j-=ymult
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
    if possible==[]: possible="none"
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
        ret+=" ("+translateMoveMade([possiblePieces[piece].x,possiblePieces[piece].y])+"), "
    return ret[:-2]
def display():
    global board
    print("   ┌───"+"┬───"*(board[0]-1)+"┐")
    for y in range(board[1],0,-1):
        print(" ",end=fill(y,2))
        for x in range(1,board[0]+1):
            print(end="│ ")
            piece=check([x,y])
            if piece!="none":
                if piece.alive:
                    if piece.color=="w": color="\033[33m"
                    else: color="\033[31m"
                    name=color+piece.displayName
                else: name=" "
            else: name=" "
            print(name,end="\033[m")
            print(end=" ")
        print("│")
        if y!=1: print("   ├───"+"┼───"*(board[0]-1)+"┤")
        else: continue
    print("   └───"+"┴───"*(board[0]-1)+"┘")
    print(end="  ")
    for x in range(1,board[0]+1): print("   ",end=intToAlphabet(x))
    print("")
def move(piece):
    global board
    possible=[]
    if piece.alive:
        if piece.piece=="King":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False,1,1)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,1,1)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,1,1)
            for i in range(piece.x-1,0,-1):
                check=check([i,piece.y])
                if check!="none":
                    if check.piece!="Rook" or check.color!=piece.color or check.hasMoved:
                        break
                    clone()
                    piece.x-=1
                    if not kingcheck(piece.color): possible.append([piece.x-2,piece.y])
                    declone()
            for i in range(piece.x+1,0,+1):
                check=check([i,piece.y])
                if check!="none":
                    if check.piece!="Rook" or check.color!=piece.color or check.hasMoved:
                        break
                    clone()
                    piece.x+=1
                    if not kingcheck(piece.color): possible.append([piece.x+2,piece.y])
                    declone()
        elif piece.piece=="Pawn":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,0,1,ydirec=1,canCapture=False)
            if not piece.hasMoved: possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,0,2,ydirec=1,ymin=2,canCapture=False)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,1,1,ydirec=1,mustCapture=True)
            temp=check([piece.x+1,piece.y])
            if temp!="none":
                if temp.piece=="Pawn" and temp.color!=piece.color and temp.extra and moveto(piece.x+1,piece.y+colorrev(piece.color,1),piece.color,False): possible.append([piece.x+1,piece.y+colorrev(piece.color,1)])
            temp=check([piece.x-1,piece.y])
            if temp!="none":
                if temp.piece=="Pawn" and temp.color!=piece.color and temp.extra and moveto(piece.x-1,piece.y+colorrev(piece.color,1),piece.color,False): possible.append([piece.x-1,piece.y+colorrev(piece.color,1)])
        elif piece.piece=="Rook":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True)
        elif piece.piece=="Knight":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,2,1,xmult=2)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,1,2,ymult=2)
        elif piece.piece=="Bishop":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True)
        elif piece.piece=="Queen":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True)
    return possible
def reset():
    global allPieces
    for i in range(8):
        allPieces[i].reset("w","Pawn","P",i+1,2)
        allPieces[8+i].reset("b","Pawn","p",i+1,7)
    allPieces[16].reset("w","Rook","R",1,1)
    allPieces[17].reset("w","Rook","R",8,1)
    allPieces[18].reset("b","Rook","R",8,8)
    allPieces[19].reset("b","Rook","R",1,8)
    allPieces[20].reset("w","Knight","N",2,1)
    allPieces[21].reset("w","Knight","N",7,1)
    allPieces[22].reset("b","Knight","N",7,8)
    allPieces[23].reset("b","Knight","N",2,8)
    allPieces[24].reset("w","Bishop","B",3,1)
    allPieces[25].reset("w","Bishop","B",6,1)
    allPieces[26].reset("b","Bishop","B",6,8)
    allPieces[27].reset("b","Bishop","B",3,8)
    allPieces[28].reset("w","Queen","Q",4,1)
    allPieces[29].reset("b","Queen","Q",4,8)
    allPieces[30].reset("w","King","K",5,1)
    allPieces[31].reset("b","King","K",5,8)
#   ┌───┬───┬───┬───┬───┬───┬───┬───┐
# 8 │ R │ k │ B │ Q │ K │ B │ k │ R │
#   ├───┼───┼───┼───┼───┼───┼───┼───┤
# 7 │ p │ p │ p │ p │ p │ p │ p │ p │
#   ├───┼───┼───┼───┼───┼───┼───┼───┤
# 6 │   │   │   │   │   │   │   │   │
#   ├───┼───┼───┼───┼───┼───┼───┼───┤
# 5 │   │   │   │   │   │   │   │   │
#   ├───┼───┼───┼───┼───┼───┼───┼───┤
# 4 │   │   │   │   │   │   │   │   │
#   ├───┼───┼───┼───┼───┼───┼───┼───┤
# 3 │   │   │   │   │   │   │   │   │
#   ├───┼───┼───┼───┼───┼───┼───┼───┤
# 2 │ p │ p │ p │ p │ p │ p │ p │ p │
#   ├───┼───┼───┼───┼───┼───┼───┼───┤
# 1 │ R │ k │ B │ Q │ K │ B │ k │ R │
#   └───┴───┴───┴───┴───┴───┴───┴───┘
#     A   B   C   D   E   F   G   H
allPieces=[chess() for i in range(32)]
board=[8,8]
play="y"
while play=="y" or play=="Y":
    color="w"
    reset()
    while True:
        if color=="w": displayColor="White"
        else: displayColor="Black"
        display()
        if possiblePieces(color)==["none"]:
            if kingcheck(color): print("The",displayColor,"player is in checkmate!")
            else: print("Stalemate!")
            print("The",swap(displayColor,"White","Black"),"player wins!")
            break
        print("The",displayColor,"player can move the following pieces:",translatePossiblePieces(possiblePieces(color)))
        while True:
            pieceMoveMade=(input("What piece do you want to move? ").replace(" ","")).lower()
            for piece in allPieces:
                if pieceMoveMade==piece.name and piece.color==color:
                    pieceMoveMade=piece
                    break
                else: pieceMoveMade="none"
            if pieceMoveMade!="none":
                if pieceMoveMade in possiblePieces(color): break
                else: print("You can't move that piece!")
            else: print("That is not a valid piece!")
        while True:
            pieceMoveMadeMoves=move(pieceMoveMade)
            try: moveMade=translateMoveMade(input("Where do you want to move "+translatePossiblePieces([pieceMoveMade])+"? ").upper())
            except:
                print("That's not a vlaid move!")
                continue
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
            if moveMade[1]==board[0]+(colorrev(pieceMoveMade.color,(board[0]-1)/2)-((board[0]-1)/2)):
                pawnPromote=input("What do you want to promote your pawn to?").capatlize()
                while pawnPromote not in ["Queen","Rook","Bishop","Knight"]:
                    print("That's not a valid piece!")
                    pawnPromote=input("What do you want to promote your pawn to?").capatlize()
                count=1
                for piece in allPieces:
                    if piece.piece==pawnPromote: count+=1
                pieceMoveMade.piece=pawnPromote
                pieceMoveMade.name=pawnPromote.lower()+str(count)
                if pawnPromote=="Knight": pieceMoveMade.displayName="N"
                else: pieceMoveMade.displayName=pawnPromote[0]
            enPassant=check([pieceMoveMade.x,pieceMoveMade.y-colorrev(pieceMoveMade.color,1)])
            if enPassant!="none":
                if enPassant.extra and enPassant.color!=pieceMoveMade.color: enPassant.alive=False
        if pieceMoveMade.piece=="King":
            if abs(pieceMoveMade.tempx-pieceMoveMade.x)==2:
                if pieceMoveMade.tempx>pieceMoveMade.x: diff=-1
                else: diff=1
                for i in range(pieceMoveMade.tempx+diff,0,diff):
                    check=check([i,pieceMoveMade.y])
                    if check.piece=="Rook":
                        check.x=pieceMoveMade.x-diff
        for piece in allPieces:
            if piece.piece=="Pawn": pieceMoveMade.extra=False
        if not pieceMoveMade.hasMoved and pieceMoveMade.piece=="Pawn": pieceMoveMade.extra=True
        pieceMoveMade.hasMoved=True
        color=swap(color,"w","b")
        if kingcheck(color): print("The",swap(displayColor,"White","Black"),"player is in check.")
    play=input("Do you want to play again? (Y/N) ")
print("Goodbye!")
