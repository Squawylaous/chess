class chess:
    name="You're not suppossed to see this."
    color="You're not suppossed to see this."
    piece="You're not suppossed to see this."
    x=0
    y=0
    hasMoved=False #this is just for pawns and castling but you could create custom pices with it.
    alive=True
    extra=False #can be used for special things like promoting pawns, en passant, or custom things. make it a list if you need more atributes
    tempcolor="You're not suppossed to see this."
    temppiece="You're not suppossed to see this."
    tempx=0
    tempy=0
    temphasMoved=False
    tempalive=True
    tempextra=False
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
def reset():
    [wpawn1.name,wpawn1.color,wpawn1.piece,wpawn1.x,wpawn1.y]=["wpawn1","w","Pawn",1,2]
    [wpawn2.name,wpawn2.color,wpawn2.piece,wpawn2.x,wpawn2.y]=["wpawn2","w","Pawn",2,2]
    [wpawn3.name,wpawn3.color,wpawn3.piece,wpawn3.x,wpawn3.y]=["wpawn3","w","Pawn",3,2]
    [wpawn4.name,wpawn4.color,wpawn4.piece,wpawn4.x,wpawn4.y]=["wpawn4","w","Pawn",4,2]
    [wpawn5.name,wpawn5.color,wpawn5.piece,wpawn5.x,wpawn5.y]=["wpawn5","w","Pawn",5,2]
    [wpawn6.name,wpawn6.color,wpawn6.piece,wpawn6.x,wpawn6.y]=["wpawn6","w","Pawn",6,2]
    [wpawn7.name,wpawn7.color,wpawn7.piece,wpawn7.x,wpawn7.y]=["wpawn7","w","Pawn",7,2]
    [wpawn8.name,wpawn8.color,wpawn8.piece,wpawn8.x,wpawn8.y]=["wpawn8","w","Pawn",8,2]
    [wrook1.name,wrook1.color,wrook1.piece,wrook1.x,wrook1.y]=["wrook1","w","Rook",1,1]
    [wknight1.name,wknight1.color,wknight1.piece,wknight1.x,wknight1.y]=["wknight1","w","Knight",2,1]
    [wbishop1.name,wbishop1.color,wbishop1.piece,wbishop1.x,wbishop1.y]=["wbishop1","w","Bishop",3,1]
    [wrook2.name,wrook2.color,wrook2.piece,wrook2.x,wrook2.y]=["wrook2","w","Rook",8,1]
    [wknight2.name,wknight2.color,wknight2.piece,wknight2.x,wknight2.y]=["wknight2","w","Knight",7,2]
    [wbishop2.name,wbishop2.color,wbishop2.piece,wbishop2.x,wbishop2.y]=["wbishop2","w","Bishop",6,1]
    [wqueen1.name,wqueen1.color,wqueen1.piece,wqueen1.x,wqueen1.y]=["wqueen1","w","Queen",4,1]
    [wking1.name,wking1.color,wking1.piece,wking1.x,wking1.y]=["wking1","w","King",5,1]
    [bpawn1.name,bpawn1.color,bpawn1.piece,bpawn1.x,bpawn1.y]=["bpawn1","b","Pawn",8,7]
    [bpawn2.name,bpawn2.color,bpawn2.piece,bpawn2.x,bpawn2.y]=["bpawn2","b","Pawn",7,7]
    [bpawn3.name,bpawn3.color,bpawn3.piece,bpawn3.x,bpawn3.y]=["bpawn3","b","Pawn",6,7]
    [bpawn4.name,bpawn4.color,bpawn4.piece,bpawn4.x,bpawn4.y]=["bpawn4","b","Pawn",5,7]
    [bpawn5.name,bpawn5.color,bpawn5.piece,bpawn5.x,bpawn5.y]=["bpawn5","b","Pawn",4,7]
    [bpawn6.name,bpawn6.color,bpawn6.piece,bpawn6.x,bpawn6.y]=["bpawn6","b","Pawn",3,7]
    [bpawn7.name,bpawn7.color,bpawn7.piece,bpawn7.x,bpawn7.y]=["bpawn7","b","Pawn",2,7]
    [bpawn8.name,bpawn8.color,bpawn8.piece,bpawn8.x,bpawn8.y]=["bpawn8","b","Pawn",1,7]
    [brook1.name,brook1.color,brook1.piece,brook1.x,brook1.y]=["brook1","b","Rook",8,8]
    [bknight1.name,bknight1.color,bknight1.piece,bknight1.x,bknight1.y]=["bknight1","b","Knight",7,8]
    [bbishop1.name,bbishop1.color,bbishop1.piece,bbishop1.x,bbishop1.y]=["bbishop1","b","Bishop",6,8]
    [brook2.name,brook2.color,brook2.piece,brook2.x,brook2.y]=["brook2","b","Rook",1,8]
    [bknight2.name,bknight2.color,bknight2.piece,bknight2.x,bknight2.y]=["bknight2","b","Knight",2,8]
    [bbishop2.name,bbishop2.color,bbishop2.piece,bbishop2.x,bbishop2.y]=["bbishop2","b","Bishop",3,8]
    [bqueen1.name,bqueen1.color,bqueen1.piece,bqueen1.x,bqueen1.y]=["bqueen1","b","Queen",4,8]
    [bking1.name,bking1.color,bking1.piece,bking1.x,bking1.y]=["bking1","b","King",5,8]
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
    #mustCapture and canCapture are really just for pawns but i guess you could make custom pieces lol.
def linearmoveto(x,y,color,acrossx,acrossy,xlimit=False,ylimit=False,xdirec=0,ydirec=0,xmin=1,ymin=1,canJump=False,canCapture=True,mustCapture=False):
    possible=["none"]
    if xlimit:
        xplim=x+xlimit+1
        xnlim=x-xlimit-1
    else:
        xplim=9 #for customizing add a custom board size thing (or just change the 9 to one more than the x if i didnt do that)
        xnlim=0
    if ylimit:
        yplim=y+ylimit+1
        ynlim=y-ylimit-1
    else:
        yplim=9 #change this to one more than the y
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
def move(piece):
    possible=["You should not see this."]
    if piece.alive:
        if piece.piece=="Pawn":
            if linearmoveto(piece.x,piece.y,piece.color,False,True,0,1,1,canCapture=False)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True,0,1,1,canCapture=False))
            if linearmoveto(piece.x,piece.y,piece.color,True,True,1,1,1,mustCapture=True)!=["none"]: possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True,1,1,1,mustCapture=True))
            if linearmoveto(piece.x,piece.y,piece.color,False,True,0,2,1,canCapture=False)!=["none"] and not piece.hasMoved: possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True,0,2,1,canCapture=False))
            #add logic for an en passant here
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
            #add castle logic (also have to consider if knight can move)
    possible.remove("You should not see this.")
    return possible
def checkcheck(piece,possible):
    for i in possible:
        clone()
        piece.x=i[0]
        piece).y=i[1]
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
    for piece in allPieces: [piece.tempcolor,piece.temppiece,piece.tempx,piece.tempy,piece.tempalive,piece.temphasMoved,piece.tempextra]=[piece.color,piece.piece,piece.x,piece.y,piece.alive,piece.hasMoved,piece.extra]
def declone():
    for piece in allPieces: [piece.color,piece.piece,piece.x,piece.y,piece.alive,piece.hasMoved,piece.extra]=[piece.tempcolor,piece.temppiece,piece.tempx,piece.tempy,piece.tempalive,piece.temphasMoved,piece.tempextra]
def translateMoveMade(moveMade):
    if isinstance(moveMade[0],int): moveMade=intToAlphabet(moveMade[0])+","+str(moveMade[1])
    else: moveMade=[alphabetToInt(moveMade[:moveMade.index(",")+1]),int(moveMade[moveMade.index(","):])]
    return moveMade
def translatePossiblePieces(possiblePieces):
    ret=""
    for piece in range(len(possiblePieces)):
        ret+=piece.piece+" "
        for char in possiblePieces[piece]:
            if char.isdigit(): ret+=char
        ret+=", "
    return ret[:-2]
def display():
    pass
    #♔♕♖♗♘♙♚♛♜♝♞♟︎
allPieces=[wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wrook1,wknight1,wbishop1,wrook2,wknight2,wbishop2,wqueen1,wking1,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,brook1,bknight1,bbishop1,brook2,bknight2,bbishop2,bqueen1,bking1]
wpawn1=chess()
wpawn2=chess()
wpawn3=chess()
wpawn4=chess()
wpawn5=chess()
wpawn6=chess()
wpawn7=chess()
wpawn8=chess()
wrook1=chess()
wknight1=chess()
wbishop1=chess()
wrook2=chess()
wknight2=chess()
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
bknight1=chess()
bbishop1=chess()
brook2=chess()
bknight2=chess()
bbishop2=chess()
bqueen1=chess()
bking1=chess()
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
        [pieceMoveMade.x,pieceMoveMade.y]=moveMade
        if check(moveMade)!=["none"]: check(moveMade).alive=False
        if pieceMoveMade.piece=="Pawn":
            if moveMade[1]==8+(colorrev(pieceMoveMade.color,3.5)-3.5): pieceMoveMade.piece=input("What do you wan to promote your pawn to?")
            if not pieceMoveMade.hasMoved: pieceMoveMade.extra=True #for en passant
        for piece in allPieces: 
            if piece.piece=="Pawn": piece.extra=False
        pieceMoveMade.hasMoved=True
        display()
        color=swap(color,"w","b")
        if kingcheck(color): print("The",color,"player is in check.")
    play=input("Do you want to play again? (Y/N) ")
print("Goodbye!")
