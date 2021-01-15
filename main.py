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
        if xy==[piece.x,piece.y]and piece.alive: ret=piece
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
        global allPieces,board
        for piece in allPieces: piece.clone()
        if check(i)!="none": check(i).alive=False
        piece.x=i[0]
        piece.y=i[1]
        if kingcheck(piece.color): possible.remove(i)
        elif i[0]<1 or i[0]>board[0] or i[1]<1 or i[1]>board[1]: possible.remove(i)
        for piece in allPieces: piece.declone()
    return possible
def possiblePieces(color):
    global allPieces
    possible=["none"]
    if color=="w":
        for piece in allPieces:
            if checkcheck(piece,move(piece)) and piece.color=="w": possible.append(piece)
    else:
        for piece in allPieces:
            if checkcheck(piece,move(piece)) and piece.color=="b": possible.append(piece)
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
    for y in range(board[1],0,-1):
        for x in range(1,board[0]+1):
            if check([x,y])!="none": name=check([x,y]).name
            else: name="No piece"
            print(name+" is at "+str(x)+","+str(y))
    pass
    #♔♕♖♗♘♙♚♛♜♝♞♟ 
def move(piece):
    global board
    possible=["You should not see this."]
    if piece.alive:
        if piece.piece=="Pawn":
            if linearmoveto(piece.x,piece.y,piece.color,False,True,0,1,1,canCapture=False)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True,0,1,1,canCapture=False))
            if linearmoveto(piece.x,piece.y,piece.color,True,True,1,1,1,mustCapture=True)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True,1,1,1,mustCapture=True))
            if linearmoveto(piece.x,piece.y,piece.color,False,True,0,2,1,xmin=2,canCapture=False)!=["none"] and not piece.hasMoved: possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True,0,2,1,canCapture=False))
            if check([piece.x+1,piece.y+colorrev(piece.color,1)])!="none":
                if check([piece.x+1,piece.y+colorrev(piece.color,1)]).color!=piece.color and check([piece.x+1,piece.y+colorrev(piece.color,1)]).piece=="Pawn" and check([piece.x+1,piece.y+colorrev(piece.color,1)]).extra: possible.append([piece.x+1,piece.y+colorrev(piece.color,1)])
            if check([piece.x-1,piece.y+colorrev(piece.color,1)])!="none":
                if check([piece.x-1,piece.y+colorrev(piece.color,1)]).color!=piece.color and check([piece.x-1,piece.y+colorrev(piece.color,1)]).piece=="Pawn" and check([piece.x-1,piece.y+colorrev(piece.color,1)]).extra: possible.append([piece.x-1,piece.y+colorrev(piece.color,1)])
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
                if not piece.hasMoved and moveto(piece.x+1,piece.y,piece.color) and moveto(piece.x+2,piece.y,piece.color) and not check([board[0],piece.y]).hasMoved and linearmoveto(board[0],check([board[0],piece.y]).y,check([board[0],piece.y]).color,True,False,abs(board[0]-piece.x)-1,xmin=abs(board[0]-piece.x)-1)!="none": possible.append([piece.x+2,piece.y])
            if check([1,piece.y])!="none":
                if not piece.hasMoved and moveto(piece.x-1,piece.y,piece.color) and moveto(piece.x-2,piece.y,piece.color) and not check([1,piece.y]).hasMoved and linearmoveto(1,check([1,piece.y]).y,check([1,piece.y]).color,True,False,abs(1-piece.x)-1,xmin=abs(1-piece.x)-1)!="none": possible.append([piece.x-2,piece.y])
    possible.remove("You should not see this.")
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
        print("You can move the following pieces:",translatePossiblePieces(possiblePieces(color)))
        while True:
            global allPieces
            pieceMoveMade=color+input("What piece do you want to move? ").strip(" ").lower()
            for piece in allPieces:
                if pieceMoveMade==piece.name: pieceMoveMade=piece
            if pieceMoveMade!="none":
                if pieceMoveMade in possiblePieces(color): break
                else: print("You can't move that piece!")
            else: print("That is not a valid piece!")
        while True:
            moveMade=translateMoveMade(input("Where do you want to move "+translatePossiblePieces([pieceMoveMade])+"? "+str(checkcheck(pieceMoveMade.color,move(pieceMoveMade)))+" lmao "+str(move(pieceMoveMade))+" "))
            if moveMade not in move(pieceMoveMade):
                print("That's not a vlaid move!")
                continue
            elif moveMade not in checkcheck(pieceMoveMade,move(pieceMoveMade)):
                print("That would put your king in check!")
                continue
            else: 
                print(translatePossiblePieces([pieceMoveMade]),"moved to",translateMoveMade(moveMade))
                break
        if pieceMoveMade.piece=="King": pieceMoveMade.tempx=pieceMoveMade.x
        [pieceMoveMade.x,pieceMoveMade.y]=moveMade
        if check(moveMade)!=["none"]: check(moveMade).alive=False
        if pieceMoveMade.piece=="Pawn":
            if check([pieceMoveMade.x,pieceMoveMade.y-colorrev(piece.color,1)])!="none":
                if check([pieceMoveMade.x,pieceMoveMade.y-colorrev(piece.color,1)]).piece=="Pawn" and check([pieceMoveMade.x,pieceMoveMade.y-colorrev(piece.color,1)]).extra: check([pieceMoveMade.x,pieceMoveMade.y-colorrev(piece.color,1)]).alive=False
            if moveMade[1]==board[0]+(colorrev(pieceMoveMade.color,(board[0]-1)/2)-1*((board[0]-1)/2)): pieceMoveMade.piece=input("What do you wan to promote your pawn to?")
            if not pieceMoveMade.hasMoved: pieceMoveMade.extra=True
            else: pieceMoveMade.extra=False
        if pieceMoveMade.piece=="King" and abs(pieceMoveMade.tempx-pieceMoveMade.x)==2:
            if pieceMoveMade.tempx-pieceMoveMade.x<0: check(1,pieceMoveMade.y).x=pieceMoveMade.x-1
            elif pieceMoveMade.tempx-pieceMoveMade.x>0: check(board[0],pieceMoveMade.y).x=pieceMoveMade.x+1
        pieceMoveMade.hasMoved=True
        color=swap(color,"w","b")
        if kingcheck(color): print("The",color,"player is in check.")
    play=input("Do you want to play again? (Y/N) ")
print("Goodbye!")
