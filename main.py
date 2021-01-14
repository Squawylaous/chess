class chess:
    name="You're not suppossed to see this."
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
    def reset(self,name,color,piece,x,y,extra):
        self.name=name
        self.color=color
        self.piece=piece
        self.x=x
        self.y=y
        self.hasMoved=False
        slef.alive=True
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
def alphabetToInt(x):
    alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    ret=0
    x=rev(x)
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
        if xy==[piece.x,piece.y]and piece.alive: ret=piece
    return ret
def kingcheck(color):
    global allPieces
    ret=False
    if color=="b":
        xy=[bking1.x,bking1.y]
        for piece in allPieces:
            if xy in move(piece): ret=True
    else:
        xy=[wking1.x,wking1.y]
        for piece in allPieces:
            if xy in move(piece): ret=True
    return ret
def moveto(x,y,color,canCapture=True,mustCapture=False):
    if (check([x,y])=="none" and not mustCapture): return True
    elif not isinstance(check([x,y]),str):
        if (check([x,y]).color!=color and canCapture): return True 
    else: return False
def linearmoveto(x,y,color,acrossx,acrossy,xlimit=False,ylimit=False,xdirec=0,ydirec=0,xmin=1,ymin=1,canJump=False,canCapture=True,mustCapture=False):
    global board
    possible=["none"]
    if xlimit:
        xplim=x+xlimit+1
        xnlim=x-xlimit-1
    else:
        xplim=board[0]
        xnlim=0
    if ylimit:
        yplim=y+ylimit+1
        ynlim=y-ylimit-1
    else:
        yplim=board[1]
        ynlim=0
    if acrossx and not acrossy:
        if xdirec>=0:
            for i in range(x+colorrev(color,xmin),xplim,colorrev(color,1)):
                if moveto(i,y,color,canCapture,mustCapture): possible.append([i,y])
                elif not canJump: break
        if xdirec<=0:
            for i in range(x-colorrev(color,xmin),xnlim,colorrev(color,-1)):
                if moveto(i,y,color,canCapture,mustCapture): possible.append([i,y])
                elif not canJump: break
    if acrossy and not acrossx:
        if ydirec>=0:
            for i in range(y+colorrev(color,ymin),yplim,colorrev(color,1)):
                if moveto(x,i,color,canCapture,mustCapture): possible.append([x,i])
                elif not canJump: break
        if ydirec<=0:
            for i in range(y-colorrev(color,xmin),ynlim,colorrev(color,-1)):
                if moveto(x,i,color,canCapture,mustCapture): possible.append([x,i])
                elif not canJump: break
    if acrossx and acrossy:
        if ydirec>=0:
            if xdirec>=0:
                j=y+ymin
                for i in range(x+colorrev(color,xmin),xplim,colorrev(color,1)):
                    if moveto(i,j,color,canCapture,mustCapture): possible.append([i,j])
                    elif not canJump: break
                    j+=1
                    if j==yplim: break
            if xdirec<=0:
                j=y+ymin
                for i in range(x-colorrev(color,xmin),xnlim,colorrev(color,-1)):
                    if moveto(i,j,color,canCapture,mustCapture): possible.append([i,j])
                    elif not canJump: break
                    j+=1
                    if j==yplim:break
        if ydirec>=0:
            if xdirec>=0:
                j=y-ymin
                for i in range(x+colorrev(color,xmin),xplim,colorrev(color,1)):
                    if moveto(i,j,color,canCapture,mustCapture): possible.append([i,j])
                    elif not canJump: break
                    j-=1
                    if j==ynlim: break
            if xdirec<=0:
                j=y-ymin
                for i in range(x-colorrev(color,xmin),xnlim,colorrev(color,-1)):
                    if moveto(i,j,color,canCapture,mustCapture): possible.append([i,j])
                    elif not canJump: break
                    j-=1
                    if j==ynlim:break
    if len(possible)>1:possible.remove("none")
    return possible
def checkcheck(piece,possible):
    for i in possible:
        clone()
        piece.x=i[0]
        piece.y=i[1]
        if check(i)!=["none"]: check(i).alive=False
        if kingcheck(piece.color): possible.remove(i)
        declone()
    return possible
def possiblePieces(color):
    possible=["none"]
    if color=="w":
        for piece in allPieces:
            if checkcheck(piece,move(piece)) and piece.color=="w": possible.append(piece)
    else:
        for piece in allPieces:
            if checkcheck(piece,move(piece)) and piece.color=="b": possible.append(piece)
    if len(possible)>1:possible.remove("none")
    return possible
def clone():
    for piece in allPieces: piece.clone()
def declone():
    for piece in allPieces: piece.declone()
def translateMoveMade(moveMade):
    if isinstance(moveMade[0],int): moveMade=intToAlphabet(moveMade[0])+","+str(moveMade[1])
    else: moveMade=[alphabetToInt(moveMade[:moveMade.index(",")+1]),int(moveMade[moveMade.index(","):])]
    return moveMade
def translatePossiblePieces(possiblePieces):
    ret=""
    for piece in range(len(possiblePieces)):
        ret+=piece.piece+" "
        for char in possiblePieces[piece].name:
            if char.isdigit(): ret+=char
        ret+=", "
    return ret[:-2]
def display():
    pass
    #♔♕♖♗♘♙♚♛♜♝♞♟ 
def move(piece):
    global board
    possible=["You should not see this."]
    if piece.alive:
        if piece.piece=="Pawn":
            if linearmoveto(piece.x,piece.y,piece.color,False,True,0,1,1,canCapture=False)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True,0,1,1,canCapture=False))
            if linearmoveto(piece.x,piece.y,piece.color,True,True,1,1,1,mustCapture=True)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True,1,1,1,mustCapture=True))
            if linearmoveto(piece.x,piece.y,piece.color,False,True,0,2,1,canCapture=False)!=["none"] and not piece.hasMoved: possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True,0,2,1,canCapture=False))
            if check([piece.x+1,piece.y+colorrev(1)])!="none":
                if check([piece.x+1,piece.y+colorrev(1)]).color!=piece.color and check([piece.x+1,piece.y+colorrev(1)]).piece=="Pawn" and check([piece.x+1,piece.y+colorrev(1)]).extra: possible.append[(piece.x+1,piece.y+colorrev(1)])
            if check([piece.x-1,piece.y+colorrev(1)])!="none":
                if check([piece.x-1,piece.y+colorrev(1)]).color!=piece.color and check([piece.x-1,piece.y+colorrev(1)]).piece=="Pawn" and check([piece.x-1,piece.y+colorrev(1)]).extra: possible.append([piece.x-1,piece.y+colorrev(1)])
        elif piece.piece=="Rook":
            if linearmoveto(piece.x,piece.y,piece.color,True,False)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False))
            if linearmoveto(piece.x,piece.y,piece.color,False,True)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True))
        elif piece.piece=="Knight":
            if linearmoveto(piece.x,piece.y,piece.color,True,True,1,2,ymin=2,canJump=True)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True,1,2,canJump=True))
            if linearmoveto(piece.x,piece.y,piece.color,True,True,2,1,xmin=2,canJump=True)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True,2,1,canJump=True))
        elif piece.piece=="Bishop":
            if linearmoveto(piece.x,piece.y,piece.color,True,True)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True))
        elif piece.piece=="Queen":
            if linearmoveto(piece.x,piece.y,piece.color,True,False)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False))
            if linearmoveto(piece.x,piece.y,piece.color,False,True)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True))
            if linearmoveto(piece.x,piece.y,piece.color,True,True)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True))
        elif piece.piece=="King":
            if linearmoveto(piece.x,piece.y,piece.color,True,False,1,1)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,1,1))
            if linearmoveto(piece.x,piece.y,piece.color,False,True,1,1)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True,1,1))
            if linearmoveto(piece.x,piece.y,piece.color,True,True,1,1)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True,1,1))
            if check([board[0],piece.y])!="none":
                if not piece.hasMoved and moveto(piece.x+1,piece.y,piece.color) and moveto(piece.x+2,piece.y,piece.color) and not check([board[0],piece.y]).hasMoved and linearmoveto(board[0],check([board[0],piece.y]).y,check([board[0],piece.y]).color,True,False,abs(board[0]-piece.x)-1,xmin=abs(board[0]-piece.x)-1)!="none": possible.append(piece.x+2,piece.y)
            if check([1,piece.y])!="none":
                if not piece.hasMoved and moveto(piece.x-1,piece.y,piece.color) and moveto(piece.x-2,piece.y,piece.color) and not check([1,piece.y]).hasMoved and linearmoveto(1,check([1,piece.y]).y,check([1,piece.y]).color,True,False,abs(1-piece.x)-1,xmin=abs(1-piece.x)-1)!="none": possible.append(piece.x-2,piece.y)
    possible.remove("You should not see this.")
    return possible
def reset():
    wpawn1.reset("wpawn1","w","Pawn",1,2)
    wpawn2.reset("wpawn2","w","Pawn",2,2)
    wpawn3.reset("wpawn3","w","Pawn",3,2)
    wpawn4.reset("wpawn4","w","Pawn",4,2)
    wpawn5.reset("wpawn5","w","Pawn",5,2)
    wpawn6.reset("wpawn6","w","Pawn",6,2)
    wpawn7.reset("wpawn7","w","Pawn",7,2)
    wpawn8.reset("wpawn8","w","Pawn",8,2)
    wrook1.reset("wrook1","w","Rook",1,1)
    wrook2.reset("wrook2","w","Rook",8,1)
    wknight1.reset("wknight1","w","Knight",2,1)
    wknight2.reset("wknight2","w","Knight",7,2)
    wbishop1.reset("wbishop1","w","Bishop",3,1)
    wbishop2.reset("wbishop2","w","Bishop",6,1)
    wqueen1.reset("wqueen1","w","Queen",4,1)
    wking1.reset("wking1","w","King",5,1)
    bpawn1.reset("bpawn1","b","Pawn",8,7)
    bpawn2.reset("bpawn2","b","Pawn",7,7)
    bpawn3.reset("bpawn3","b","Pawn",6,7)
    bpawn4.reset("bpawn4","b","Pawn",5,7)
    bpawn5.reset("bpawn5","b","Pawn",4,7)
    bpawn6.reset("bpawn6","b","Pawn",3,7)
    bpawn7.reset("bpawn7","b","Pawn",2,7)
    bpawn8.reset("bpawn8","b","Pawn",1,7)
    brook1.reset("brook1","b","Rook",8,8)
    brook2.reset("brook2","b","Rook",1,8)
    bknight1.reset("bknight1","b","Knight",7,8)
    bknight2.reset("bknight2","b","Knight",2,8)
    bbishop1.reset("bbishop1","b","Bishop",6,8)
    bbishop2.reset("bbishop2","b","Bishop",3,8)
    bqueen1.reset("bqueen1","b","Queen",4,8)
    bking1.reset("bking1","b","King",5,8)
wpawn1=chess()
wpawn2=chess()
wpawn3=chess()
wpawn4=chess()
wpawn5=chess()
wpawn6=chess()
wpawn7=chess()
wpawn8=chess()
wrook1=chess()
wrook2=chess()
wknight1=chess()
wknight2=chess()
wbishop1=chess()
wbishop2=chess()
wqueen1=chess()
wking1=chess()
bpawn1=chess()
bpawn2=chess()
bpawn3=chess()
bpawn4=chess()
bpawn5=chess()
bpawn6=chess()
bpawn7=chess()
bpawn8=chess()
brook1=chess()
brook2=chess()
bknight1=chess()
bknight2=chess()
bbishop1=chess()
bbishop2=chess()
bqueen1=chess()
bking1=chess()
allPieces=[wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wrook1,wknight1,wbishop1,wrook2,wknight2,wbishop2,wqueen1,wking1,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,brook1,bknight1,bbishop1,brook2,bknight2,bbishop2,bqueen1,bking1]
board=[8,8]
play="y"
while play=="y" or play=="Y":
    color="w"
    reset()
    while True:
        if possiblePieces(color)==["none"]:
            if kingcheck(color): print("The",color,"player is in checkmate!")
            else: print("Stalemate!")
            print("The",swap(color,"w","b"),"player wins!")
            break
        print("You can move the following pieces:",translatePossiblePieces(possiblePieces(color)))
        while True:
            pieceMoveMade=color+input("What piece do you want to move? ").strip(" ").lower()
            for piece in allPieces:
                if pieceMoveMade==piece.name: pieceMoveMade=piece
            if pieceMoveMade!="none":
                if pieceMoveMade in possiblePieces: break
                else: print("You can't move that piece!")
            else: print("That is not a valid piece!")
        while True:
            moveMade=translateMoveMade(input("Where do you want to move "+pieceMoveMade+"? "))
            if moveMade not in move(pieceMoveMade):
                print("That's not a vlaid move!")
                continue
            elif moveMade not in checkcheck(pieceMoveMade,move(pieceMoveMade)):
                print("That would put your king in check!")
                continue
            else: 
                print(pieceMoveMade,"moved to",translateMoveMade(moveMade))
                break
        if pieceMoveMade.piece=="King": pieceMoveMade.tempx=pieceMoveMade.x
        [pieceMoveMade.x,pieceMoveMade.y]=moveMade
        if check(moveMade)!=["none"]: check(moveMade).alive=False
        if pieceMoveMade.piece=="Pawn":
            if check([pieceMoveMade.x,pieceMoveMade.y-colorrev(1)])!="none":
                if check([pieceMoveMade.x,pieceMoveMade.y-colorrev(1)]).piece=="Pawn" and check([pieceMoveMade.x,pieceMoveMade.y-colorrev(1)]).extra: check([pieceMoveMade.x,pieceMoveMade.y-colorrev(1)]).alive=False
            if moveMade[1]==board[0]+(colorrev(pieceMoveMade.color,(board[0]-1)/2)-1*((board[0]-1)/2)): pieceMoveMade.piece=input("What do you wan to promote your pawn to?")
            if not pieceMoveMade.hasMoved: pieceMoveMade.extra=True
            else: pieceMoveMade.extra=False
        if pieceMoveMade.piece=="King" and abs(pieceMoveMade.tempx-pieceMoveMade.x)==2:
            if pieceMoveMade.tempx-pieceMoveMade.x<0: check(1,pieceMoveMade.y).x=pieceMoveMade.x-1
            elif pieceMoveMade.tempx-pieceMoveMade.x>0: check(board[0],pieceMoveMade.y).x=pieceMoveMade.x+1
        pieceMoveMade.hasMoved=True
        display()
        color=swap(color,"w","b")
        if kingcheck(color): print("The",color,"player is in check.")
    play=input("Do you want to play again? (Y/N) ")
print("Goodbye!")
