class chess:
    color="You're not suppossed to see this."
    piece="You're not suppossed to see this."
    x=0
    y=0
    hasMoved=False #this is just for pawns and castling but you could create custom pices with it. also might have to add a times moved for en passant
    alive=True
def swap(swap,x,y):
    if swap==x: return y
    if swap==y: return x
def pos(piece,x,y): [piece.x,piece.y]=[x,y]
def create(piece,c,p,x,y):
    [piece.color,piece.piece,piece.x,piece.y]=[c,p,x,y]
    return piece
def reset():
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking
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
    if xy==[wpawn1.x,wpawn1.y] and wpawn1.alive: return "wpawn1"
    elif xy==[wpawn2.x,wpawn2.y] and wpawn2.alive: return "wpawn2"
    elif xy==[wpawn3.x,wpawn3.y] and wpawn3.alive: return "wpawn3"
    elif xy==[wpawn4.x,wpawn4.y] and wpawn4.alive: return "wpawn4"
    elif xy==[wpawn5.x,wpawn5.y] and wpawn5.alive: return "wpawn5"
    elif xy==[wpawn6.x,wpawn6.y] and wpawn6.alive: return "wpawn6"
    elif xy==[wpawn7.x,wpawn7.y] and wpawn7.alive: return "wpawn7"
    elif xy==[wpawn8.x,wpawn8.y] and wpawn8.alive: return "wpawn8"
    elif xy==[wlrook.x,wlrook.y] and wlrook.alive: return "wlrook"
    elif xy==[wlknight.x,wlknight.y] and wlknight.alive: return "wlknight"
    elif xy==[wlbishop.x,wlbishop.y] and wlbishop.alive: return "wlbishop"
    elif xy==[wrrook.x,wrrook.y] and wrrook.alive: return "wrrook"
    elif xy==[wrknight.x,wrknight.y] and wrknight.alive: return "wrknight"
    elif xy==[wrbishop.x,wrbishop.y] and wrbishop.alive: return "wrbishop"
    elif xy==[wqueen.x,wqueen.y] and wqueen.alive: return "wqueen"
    elif xy==[wking.x,wking.y] and wking.alive: return "wking"
    elif xy==[bpawn1.x,bpawn1.y] and bpawn1.alive: return "bpawn1"
    elif xy==[bpawn2.x,bpawn2.y] and bpawn2.alive: return "bpawn2"
    elif xy==[bpawn3.x,bpawn3.y] and bpawn3.alive: return "bpawn3"
    elif xy==[bpawn4.x,bpawn4.y] and bpawn4.alive: return "bpawn4"
    elif xy==[bpawn5.x,bpawn5.y] and bpawn5.alive: return "bpawn5"
    elif xy==[bpawn6.x,bpawn6.y] and bpawn6.alive: return "bpawn6"
    elif xy==[bpawn7.x,bpawn7.y] and bpawn7.alive: return "bpawn7"
    elif xy==[bpawn8.x,bpawn8.y] and bpawn8.alive: return "bpawn8"
    elif xy==[blrook.x,blrook.y] and blrook.alive: return "blrook"
    elif xy==[blknight.x,blknight.y] and blknight.alive: return "blknight"
    elif xy==[blbishop.x,blbishop.y] and blbishop.alive: return "blbishop"
    elif xy==[brrook.x,brrook.y] and brrook.alive: return "brrook"
    elif xy==[brknight.x,brknight.y] and brknight.alive: return "brknight"
    elif xy==[brbishop.x,brbishop.y] and brbishop.alive: return "brbishop"
    elif xy==[bqueen.x,bqueen.y] and bqueen.alive: return "bqueen"
    elif xy==[bking.x,bking.y] and bking.alive: return "bking"
    return "none"
def kingcheck(color):
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking
    if color=="b":
        xy=[bking.x,bking.y]
        if xy in move(wpawn1): return True
        elif xy in move(wpawn2.x,wpawn2.y): return True
        elif xy in move(wpawn3.x,wpawn3.y): return True
        elif xy in move(wpawn4.x,wpawn4.y): return True
        elif xy in move(wpawn5.x,wpawn5.y): return True
        elif xy in move(wpawn6.x,wpawn6.y): return True
        elif xy in move(wpawn7.x,wpawn7.y): return True
        elif xy in move(wpawn8.x,wpawn8.y): return True
        elif xy in move(wlrook.x,wlrook.y): return True
        elif xy in move(wlknight.x,wlknight.y): return True
        elif xy in move(wlbishop.x,wlbishop.y): return True
        elif xy in move(wrrook.x,wrrook.y): return True
        elif xy in move(wrknight.x,wrknight.y): return True
        elif xy in move(wrbishop.x,wrbishop.y): return True
        elif xy in move(wqueen.x,wqueen.y): return True
        elif xy in move(wking.x,wking.y): return True
        else: return False
    else:
        xy=[wking.x,wking.y]
        if xy in move(bpawn1.x,bpawn1.y): return True
        elif xy in move(bpawn2.x,bpawn2.y): return True
        elif xy in move(bpawn3.x,bpawn3.y): return True
        elif xy in move(bpawn4.x,bpawn4.y): return True
        elif xy in move(bpawn5.x,bpawn5.y): return True
        elif xy in move(bpawn6.x,bpawn6.y): return True
        elif xy in move(bpawn7.x,bpawn7.y): return True
        elif xy in move(bpawn8.x,bpawn8.y): return True
        elif xy in move(blrook.x,blrook.y): return True
        elif xy in move(blknight.x,blknight.y): return True
        elif xy in move(blbishop.x,blbishop.y): return True
        elif xy in move(brrook.x,brrook.y): return True
        elif xy in move(brknight.x,brknight.y): return True
        elif xy in move(brbishop.x,brbishop.y): return True
        elif xy in move(bqueen.x,bqueen.y): return True
        elif xy in move(bking.x,bking.y): return True
        else: return False
def moveto(x,y,color,canCapture=True,mustCapture=False):
    if (check([x,y])=="none" and not mustCapture): return True
    elif not isinstance(check([x,y]),str):
        if (check([x,y]).color!=color and canCapture): return True 
    else: return False
    #mustCapture and canCapture are really just for pawns but i guess you could make custom pieces lol.
def linearmoveto(x,y,color,acrossx,acrossy,xlimit=False,ylimit=False,canCapture=True,mustCapture=False):
    #add a directional specifier for x and y (x/ydirec?), minimun movement (x/ymin) and if movement can pass through peices
    possible=["You should not see this."]
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
        for i in range(x+1,xplim):
            if moveto(i,y,color,canCapture,mustCapture): possible.append([i,y])
        for i in range(x-1,xnlim,-1):
            if moveto(i,y,color,canCapture,mustCapture): possible.append([i,y])
    elif acrossy and not acrossx:
        for i in range(y+1,yplim):
            if moveto(i,y,color,canCapture,mustCapture): possible.append([x,i])
        for i in range(y-1,ynlim,-1):
            if moveto(i,y,color,canCapture,mustCapture): possible.append([x,i])
    elif acrossx and acrossy:
        j=y+1
        for i in range(x+1,xplim):
            if moveto(i,j,color,canCapture,mustCapture): possible.append([i,j])
            j+=1
            if j==yplim: break
        j=y+1
        for i in range(x-1,xnlim,-1):
            if moveto(i,j,color,canCapture,mustCapture): possible.append([i,j])
            j+=1
            if j==yplim:break
        j=y-1
        for i in range(x+1,xplim):
            if moveto(i,j,color,canCapture,mustCapture): possible.append([i,j])
            j-=1
            if j==ynlim: break
        j=y-1
        for i in range(x-1,xnlim,-1):
            if moveto(i,j,color,canCapture,mustCapture): possible.append([i,j])
            j-=1
            if j==ynlim:break
    return possible.remove("You should not see this.")
def move(piece):
    possible=["You should not see this."]
    if piece.alive:
        if piece.piece=="Pawn":
            if moveto(piece.x,piece.y+colorrev(piece.color,1),piece.color,False): possible.append([piece.x,piece.y+colorrev(piece.color,1)])
            if moveto(piece.x+1,piece.y+colorrev(piece.color,1),piece.color,True,True): possible.append([piece.x+1,piece.y+colorrev(piece.color,1)])
            if moveto(piece.x-1,piece.y+colorrev(piece.color,1),piece.color,True,True): possible.append([piece.x-1,piece.y+colorrev(piece.color,1)])
            if moveto(piece.x,piece.y+colorrev(piece.color,1),piece.color,False) and moveto(piece.x,piece.y+colorrev(piece.color,2),piece.color,False) and not piece.hasMoved: possible.append([piece.x,piece.y+colorrev(piece.color,2)])
            #add logic for an en passant here
        elif piece.piece=="Rook":
            if linearmoveto(piece.x,piece.y,piece.color,True,False): possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False))
            if linearmoveto(piece.x,piece.y,piece.color,False,True): possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True))
        elif piece.piece=="Knight":
            if moveto(piece.x+1,piece.y+2,piece.color): possible.append([piece.x+1,piece.y+2])
            if moveto(piece.x-1,piece.y+2,piece.color): possible.append([piece.x-1,piece.y+2])
            if moveto(piece.x+1,piece.y-2,piece.color): possible.append([piece.x+1,piece.y-2])
            if moveto(piece.x-1,piece.y-2,piece.color): possible.append([piece.x-1,piece.y-2])
            if moveto(piece.x+2,piece.y+1,piece.color): possible.append([piece.x+2,piece.y+1])
            if moveto(piece.x-2,piece.y+1,piece.color): possible.append([piece.x-2,piece.y+1])
            if moveto(piece.x+2,piece.y-1,piece.color): possible.append([piece.x+2,piece.y-1])
            if moveto(piece.x-2,piece.y-1,piece.color): possible.append([piece.x-2,piece.y-1])
        elif piece.piece=="Bishop":
            if linearmoveto(piece.x,piece.y,piece.color,True,True): possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True))
        elif piece.piece=="Queen":
            if linearmoveto(piece.x,piece.y,piece.color,True,False): possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False))
            if linearmoveto(piece.x,piece.y,piece.color,False,True): possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True))
            if linearmoveto(piece.x,piece.y,piece.color,True,True): possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True))
        elif piece.piece=="King":
            if linearmoveto(piece.x,piece.y,piece.color,True,False,1,1): possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,False,1,1))
            if linearmoveto(piece.x,piece.y,piece.color,False,True,1,1): possible.extend(linearmoveto(piece.x,piece.y,piece.color,False,True,1,1))
            if linearmoveto(piece.x,piece.y,piece.color,True,True,1,1): possible.extend(linearmoveto(piece.x,piece.y,piece.color,True,True,1,1))
            #add castle logic (also have to consider if knight can move)
    possible.remove("You should not see this.")
    return possible
def find(piece):
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking
    if piece=="wpawn1": return wpawn1
    elif piece=="wpawn2": return wpawn2
    elif piece=="wpawn3": return wpawn3
    elif piece=="wpawn4": return wpawn4
    elif piece=="wpawn5": return wpawn5
    elif piece=="wpawn6": return wpawn6
    elif piece=="wpawn7": return wpawn7
    elif piece=="wpawn8": return wpawn8
    elif piece=="wlrook": return wlrook
    elif piece=="wlknight": return wlknight
    elif piece=="wlbishop": return wlbishop
    elif piece=="wrrook": return wrrook
    elif piece=="wrknight": return wrknight
    elif piece=="wrbishop": return wrbishop
    elif piece=="wqueen": return wqueen
    elif piece=="wking": return wking
    elif piece=="bpawn1": return bpawn1
    elif piece=="bpawn2": return bpawn2
    elif piece=="bpawn3": return bpawn3
    elif piece=="bpawn4": return bpawn4
    elif piece=="bpawn5": return bpawn5
    elif piece=="bpawn6": return bpawn6
    elif piece=="bpawn7": return bpawn7
    elif piece=="bpawn8": return bpawn8
    elif piece=="blrook": return blrook
    elif piece=="blknight": return blknight
    elif piece=="blbishop": return blbishop
    elif piece=="brrook": return brrook
    elif piece=="brknight": return brknight
    elif piece=="brbishop": return brbishop
    elif piece=="bqueen": return bqueen
    elif piece=="bking": return bking
def checkcheck(piece,possible):
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking,tempwpawn1,tempwpawn2,tempwpawn3,tempwpawn4,tempwpawn5,tempwpawn6,tempwpawn7,tempwpawn8,tempwlrook,tempwlknight,tempwlbishop,tempwrrook,tempwrknight,tempwrbishop,tempwqueen,tempwking,tempbpawn1,tempbpawn2,tempbpawn3,tempbpawn4,tempbpawn5,tempbpawn6,tempbpawn7,tempbpawn8,tempblrook,tempblknight,tempblbishop,tempbrrook,tempbrknight,tempbrbishop,tempbqueen,tempbking
    for i in possible:
        clone()
        find(piece).x=i[0]
        find(piece).y=i[1]
        find(check(i)).alive=False
        if kingcheck(find(piece).color): possible.remove(i)
        declone()
    return possible
def possiblePieces(color):
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking
    possible=[]
    if color=="w":
        if checkcheck(wpawn1,move(wpawn1)): possible.append("wpawn1")
        if checkcheck(wpawn2,move(wpawn2)): possible.append("wpawn2")
        if checkcheck(wpawn3,move(wpawn3)): possible.append("wpawn3")
        if checkcheck(wpawn4,move(wpawn4)): possible.append("wpawn4")
        if checkcheck(wpawn5,move(wpawn5)): possible.append("wpawn5")
        if checkcheck(wpawn6,move(wpawn6)): possible.append("wpawn6")
        if checkcheck(wpawn7,move(wpawn7)): possible.append("wpawn7")
        if checkcheck(wpawn8,move(wpawn8)): possible.append("wpawn8")
        if checkcheck(wlrook,move(wlrook)): possible.append("wlrook")
        if checkcheck(wlknight,move(wlknight)): possible.append("wlknight")
        if checkcheck(wlbishop,move(wlbishop)): possible.append("wlbishop")
        if checkcheck(wrrook,move(wrrook)): possible.append("wrrook")
        if checkcheck(wrknight,move(wrknight)): possible.append("wrknight")
        if checkcheck(wrbishop,move(wrbishop)): possible.append("wrbishop")
        if checkcheck(wqueen,move(wqueen)): possible.append("wqueen")
        if checkcheck(wking,move(wking)): possible.append("wking")
    else:
        if checkcheck(bpawn1,move(bpawn1)): possible.append("bpawn1")
        if checkcheck(bpawn2,move(bpawn2)): possible.append("bpawn2")
        if checkcheck(bpawn3,move(bpawn3)): possible.append("bpawn3")
        if checkcheck(bpawn4,move(bpawn4)): possible.append("bpawn4")
        if checkcheck(bpawn5,move(bpawn5)): possible.append("bpawn5")
        if checkcheck(bpawn6,move(bpawn6)): possible.append("bpawn6")
        if checkcheck(bpawn7,move(bpawn7)): possible.append("bpawn7")
        if checkcheck(bpawn8,move(bpawn8)): possible.append("bpawn8")
        if checkcheck(blrook,move(blrook)): possible.append("blrook")
        if checkcheck(blknight,move(blknight)): possible.append("blknight")
        if checkcheck(blbishop,move(blbishop)): possible.append("blbishop")
        if checkcheck(brrook,move(brrook)): possible.append("brrook")
        if checkcheck(brknight,move(brknight)): possible.append("brknight")
        if checkcheck(brbishop,move(brbishop)): possible.append("brbishop")
        if checkcheck(bqueen,move(bqueen)): possible.append("bqueen")
        if checkcheck(bking,move(bking)): possible.append("bking")
    return possible
def clone():
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking,tempwpawn1,tempwpawn2,tempwpawn3,tempwpawn4,tempwpawn5,tempwpawn6,tempwpawn7,tempwpawn8,tempwlrook,tempwlknight,tempwlbishop,tempwrrook,tempwrknight,tempwrbishop,tempwqueen,tempwking,tempbpawn1,tempbpawn2,tempbpawn3,tempbpawn4,tempbpawn5,tempbpawn6,tempbpawn7,tempbpawn8,tempblrook,tempblknight,tempblbishop,tempbrrook,tempbrknight,tempbrbishop,tempbqueen,tempbking
    tempwpawn1=wpawn1
    tempwpawn2=wpawn2
    tempwpawn3=wpawn3
    tempwpawn4=wpawn4
    tempwpawn5=wpawn5
    tempwpawn6=wpawn6
    tempwpawn7=wpawn7
    tempwpawn8=wpawn8
    tempwlrook=wlrook
    tempwlknight=wlknight
    tempwlbishop=wlbishop
    tempwrrook=wrrook
    tempwrknight=wrknight
    tempwrbishop=wrbishop
    tempwqueen=wqueen
    tempwking=wking
    tempbpawn1=bpawn1
    tempbpawn2=bpawn2
    tempbpawn3=bpawn3
    tempbpawn4=bpawn4
    tempbpawn5=bpawn5
    tempbpawn6=bpawn6
    tempbpawn7=bpawn7
    tempbpawn8=bpawn8
    tempblrook=blrook
    tempblknight=blknight
    tempblknight=blknight
    tempblbishop=blbishop
    tempbrrook=brrook
    tempbrknight=brknight
    tempbrbishop=brbishop
    tempbqueen=bqueen
    tempbking=bking
def declone():
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking,tempwpawn1,tempwpawn2,tempwpawn3,tempwpawn4,tempwpawn5,tempwpawn6,tempwpawn7,tempwpawn8,tempwlrook,tempwlknight,tempwlbishop,tempwrrook,tempwrknight,tempwrbishop,tempwqueen,tempwking,tempbpawn1,tempbpawn2,tempbpawn3,tempbpawn4,tempbpawn5,tempbpawn6,tempbpawn7,tempbpawn8,tempblrook,tempblknight,tempblbishop,tempbrrook,tempbrknight,tempbrbishop,tempbqueen,tempbking
    wpawn1=tempwpawn1
    wpawn2=tempwpawn2
    wpawn3=tempwpawn3
    wpawn4=tempwpawn4
    wpawn5=tempwpawn5
    wpawn6=tempwpawn6
    wpawn7=tempwpawn7
    wpawn8=tempwpawn8
    wlrook=tempwlrook
    wlknight=tempwlknight
    wlbishop=tempwlbishop
    wrrook=tempwrrook
    wrknight=tempwrknight
    wrbishop=tempwrbishop
    wqueen=tempwqueen
    wking=tempwking
    bpawn1=tempbpawn1
    bpawn2=tempbpawn2
    bpawn3=tempbpawn3
    bpawn4=tempbpawn4
    bpawn5=tempbpawn5
    bpawn6=tempbpawn6
    bpawn7=tempbpawn7
    bpawn8=tempbpawn8
    blrook=tempblrook
    blknight=tempblknight
    blbishop=tempblbishop
    brrook=tempbrrook
    brknight=tempbrknight
    brbishop=tempbrbishop
    bqueen=tempbqueen
    bking=tempbking
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
reset()
print("You can move the following pieces:",possiblePieces("w"))
d=input("What piece do you want to move? ")
dd=find(d)
possible=checkcheck(dd,move(dd))
print("You can move",str(dd),"from ["+str(dd.x)+","+str(dd.y)+"] to the following location(s):",possible,"\n",)
