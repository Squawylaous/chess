class chess:
    color="You're not suppossed to see this."
    piece="You're not suppossed to see this."
    x=0
    y=0
    hasMoved=False
    alive=True
def pos(piece,x,y): [piece.x,piece.y]=[x,y]
def create(piece,c,p,x,y): [piece.color,piece.piece,piece.x,piece.y]=[c,p,x,y]
def reset():
    create(wpawn1,"w","Pawn",1,2)
    create(wpawn2,"w","Pawn",2,2)
    create(wpawn3,"w","Pawn",3,2)
    create(wpawn4,"w","Pawn",4,2)
    create(wpawn5,"w","Pawn",5,2)
    create(wpawn6,"w","Pawn",6,2)
    create(wpawn7,"w","Pawn",7,2)
    create(wpawn8,"w","Pawn",8,2)
    create(wlrook,"w","Rook",1,1)
    create(wlknight,"w","Knight",2,1)
    create(wlbishop,"w","Bishop",3,1)
    create(wrrook,"w","Rook",8,1)
    create(wrknight,"w","Knight",7,1)
    create(wrbishop,"w","Bishop",6,1)
    create(wqueen,"w","Queen",4,1)
    create(wking,"w","King",5,1)
    create(bpawn1,"b","Pawn",8,7)
    create(bpawn2,"b","Pawn",7,7)
    create(bpawn3,"b","Pawn",6,7)
    create(bpawn4,"b","Pawn",5,7)
    create(bpawn5,"b","Pawn",4,7)
    create(bpawn6,"b","Pawn",3,7)
    create(bpawn7,"b","Pawn",2,7)
    create(bpawn8,"b","Pawn",1,7)
    create(blrook,"b","Rook",8,8)
    create(blknight,"b","Knight",7,8)
    create(blbishop,"b","Bishop",6,8)
    create(brrook,"b","Rook",1,8)
    create(brknight,"b","Knight",2,8)
    create(brbishop,"b","Bishop",3,8)
    create(bqueen,"b","Queen",4,8)
    create(bking,"b","King",5,8)
def colorrev(color,x):
    if color=="w": return x
    else: return -1*x
def check(xy):
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking
    if xy==[wpawn1.x,wpawn1.y] return wpawn1
    elif xy==[wpawn2.x,wpawn2.y] return wpawn2
    elif xy==[wpawn3.x,wpawn3.y] return wpawn3
    elif xy==[wpawn4.x,wpawn4.y] return wpawn4
    elif xy==[wpawn5.x,wpawn5.y] return wpawn5
    elif xy==[wpawn6.x,wpawn6.y] return wpawn6
    elif xy==[wpawn7.x,wpawn7.y] return wpawn7
    elif xy==[wpawn8.x,wpawn8.y] return wpawn8
    elif xy==[wlrook.x,wlrook.y] return wlrook
    elif xy==[wlknight.x,wlknight.y] return wlknight
    elif xy==[wlbishop.x,wlbishop.y] return wlbishop
    elif xy==[wrrook.x,wrrook.y] return wrrook
    elif xy==[wrknight.x,wrknight.y] return wrknight
    elif xy==[wrbishop.x,wrbishop.y] return wrbishop
    elif xy==[wqueen.x,wqueen.y] return wqueen
    elif xy==[wking.x,wking.y] return wking
    elif xy==[bpawn1.x,bpawn1.y] return bpawn1
    elif xy==[bpawn2.x,bpawn2.y] return bpawn2
    elif xy==[bpawn3.x,bpawn3.y] return bpawn3
    elif xy==[bpawn4.x,bpawn4.y] return bpawn4
    elif xy==[bpawn5.x,bpawn5.y] return bpawn5
    elif xy==[bpawn6.x,bpawn6.y] return bpawn6
    elif xy==[bpawn7.x,bpawn7.y] return bpawn7
    elif xy==[bpawn8.x,bpawn8.y] return bpawn8
    elif xy==[blrook.x,blrook.y] return blrook
    elif xy==[blknight.x,blknight.y] return blknight
    elif xy==[blbishop.x,blbishop.y] return blbishop
    elif xy==[brrook.x,brrook.y] return brrook
    elif xy==[brknight.x,brknight.y] return brknight
    elif xy==[brbishop.x,brbishop.y] return brbishop
    elif xy==[bqueen.x,bqueen.y] return bqueen
    elif xy==[bking.x,bking.y] return bking
    return "none"
def moveto(x,y,color,canCapture,mustCapture): #mustCapture and canCapture are really just for pawns but i guess you could make custom pieces lol.
    if (check([x,y])=="none" and not mustCapture) or (check([x,y]).c!=color and canCapture): return True 
    #gotta also check for king check
    else: return False
def linearmoveto(x,y,color,canCapture,mustCapture,acrossx,acrossy,xlimit,ylimit):
    possible=["You should not see this."]
    if xlimit:
        xplim=x+xlimit+1
        xnlim=x-xlimit-1
    else:
        xplim=9
        xnlim=0
    if ylimit:
        yplim=y+ylimit+1
        ynlim=y-ylimit-1
    else:
        yplim=9
        ynlim=0
    if acrossx and not acrossy:
        for i in range(x+1,xplim):
            if moveto(i,y,color,canCapture,mustCapture): possible.appened([i,y])
        for i in range(x-1,xnlim,-1):
            if moveto(i,y,color,canCapture,mustCapture): possible.appened([i,y])
    elif acrossy and not acrossx:
        for i in range(y+1,yplim):
            if moveto(i,y,color,canCapture,mustCapture): possible.appened([x,i])
        for i in range(y-1,ynlim,-1):
            if moveto(i,y,color,canCapture,mustCapture): possible.appened([x,i])
    elif acrossx and acrossy:
        j=y+1
        for i in range(x+1,xplim):
            if moveto(i,j,color,canCapture,mustCapture): possible.appened([i,j])
            j+=1
            if j==yplim: break
        j=y+1
        for i in range(x-1,xnlim,-1):
            if moveto(i,j,color,canCapture,mustCapture): possible.appened([i,j])
            j+=1
            if j==yplim:break
        j=y-1
        for i in range(x+1,xplim):
            if moveto(i,j,color,canCapture,mustCapture): possible.appened([i,j])
            j-=1
            if j==ynlim: break
        j=y-1
        for i in range(x-1,xnlim,-1):
            if moveto(i,j,color,canCapture,mustCapture): possible.appened([i,j])
            j-=1
            if j==ynlim:break
    return possible.remove("You should not see this.")
def move(piece):
    possible=["You should not see this."]
    if piece.piece=="Pawn":
        if moveto(piece.x+colorrev(piece.color,1),piece.y,piece.color,False,False): possible.appened([piece.x+colorrev(piece.color,1),piece.y])
        if moveto(piece.x+colorrev(piece.color,1),piece.y+1,piece.color,True,True): possible.appened([piece.x+colorrev(piece.color,1),piece.y+1])
        if moveto(piece.x+colorrev(piece.color,1),piece.y-1,piece.color,True,True): possible.appened([piece.x+colorrev(piece.color,1),piece.y-1])
        if moveto(piece.x+colorrev(piece.color,2),piece.y,piece.color,False,False) and not piece.hasMoved: possible.appened([piece.x+colorrev(piece.color,2),piece.y])
    elif piece.piece=="Rook":
        possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,True,False,False,False))
        possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,False,True,False,False))
        #add castle logic (rook moves in front of king, king jumps over rook)
    elif piece.piece=="Knight":
        if moveto(piece.x+1,piece.y+2,piece.color,True,False): possible.appened([piece.x+1,piece.y+2])
        if moveto(piece.x-1,piece.y+2,piece.color,True,False): possible.appened([piece.x-1,piece.y+2])
        if moveto(piece.x+1,piece.y-2,piece.color,True,False): possible.appened([piece.x+1,piece.y-2])
        if moveto(piece.x-1,piece.y-2,piece.color,True,False): possible.appened([piece.x-1,piece.y-2])
        if moveto(piece.x+2,piece.y+1,piece.color,True,False): possible.appened([piece.x+2,piece.y+1])
        if moveto(piece.x-2,piece.y+1,piece.color,True,False): possible.appened([piece.x-2,piece.y+1])
        if moveto(piece.x+2,piece.y-1,piece.color,True,False): possible.appened([piece.x+2,piece.y-1])
        if moveto(piece.x-2,piece.y-1,piece.color,True,False): possible.appened([piece.x-2,piece.y-1])
    elif piece.piece=="Bishop":
        possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,True,True,False,False))
    elif piece.piece=="Queen":
        possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,True,False,False,False))
        possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,False,True,False,False))
        possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,True,True,False,False))
    elif piece.piece=="King":
        possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,True,False,1,1))
        possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,False,True,1,1))
        possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,True,True,1,1))
    return possible.remove("You should not see this.")
wpawn1=chess()
wpawn2=chess()
wpawn3=chess()
wpawn4=chess()
wpawn5=chess()
wpawn6=chess()
wpawn7=chess()
wpawn8=chess()
wlrook=chess()
wlknight=chess()
wlbishop=chess()
wrrook=chess()
wrknight=chess()
wrbishop=chess()
wqueen=chess()
wking=chess()
bpawn1=chess()
bpawn2=chess()
bpawn3=chess()
bpawn4=chess()
bpawn5=chess()
bpawn6=chess()
bpawn7=chess()
bpawn8=chess()
blrook=chess()
blknight=chess()
blbishop=chess()
brrook=chess()
brknight=chess()
brbishop=chess()
bqueen=chess()
bking=chess()
