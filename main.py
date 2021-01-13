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
def reset():
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking
    [wpawn1.color,wpawn1.piece,wpawn1.x,wpawn1.y]=["w","Pawn",1,2]
    [wpawn2.color,wpawn2.piece,wpawn2.x,wpawn2.y]=["w","Pawn",2,2]
    [wpawn3.color,wpawn3.piece,wpawn3.x,wpawn3.y]=["w","Pawn",3,2]
    [wpawn4.color,wpawn4.piece,wpawn4.x,wpawn4.y]=["w","Pawn",4,2]
    [wpawn5.color,wpawn5.piece,wpawn5.x,wpawn5.y]=["w","Pawn",5,2]
    [wpawn6.color,wpawn6.piece,wpawn6.x,wpawn6.y]=["w","Pawn",6,2]
    [wpawn7.color,wpawn7.piece,wpawn7.x,wpawn7.y]=["w","Pawn",7,2]
    [wpawn8.color,wpawn8.piece,wpawn8.x,wpawn8.y]=["w","Pawn",8,2]
    [wlrook.color,wlrook.piece,wlrook.x,wlrook.y]=["w","Rook",1,1]
    [wlknight.color,wlknight.piece,wlknight.x,wlknight.y]=["w","Knight",2,1]
    [wlbishop.color,wlbishop.piece,wlbishop.x,wlbishop.y]=["w","Bishop",3,1]
    [wrrook.color,wrrook.piece,wrrook.x,wrrook.y]=["w","Rook",8,1]
    [wrknight.color,wrknight.piece,wrknight.x,wrknight.y]=["w","Knight",7,1]
    [wrbishop.color,wrbishop.piece,wrbishop.x,wrbishop.y]=["w","Bishop",6,1]
    [wqueen.color,wqueen.piece,wqueen.x,wqueen.y]=["w","Queen",4,1]
    [wking.color,wking.piece,wking.x,wking.y]=["w","King",5,1]
    [bpawn1.color,bpawn1.piece,bpawn1.x,bpawn1.y]=["b","Pawn",8,7]
    [bpawn2.color,bpawn2.piece,bpawn2.x,bpawn2.y]=["b","Pawn",7,7]
    [bpawn3.color,bpawn3.piece,bpawn3.x,bpawn3.y]=["b","Pawn",6,7]
    [bpawn4.color,bpawn4.piece,bpawn4.x,bpawn4.y]=["b","Pawn",5,7]
    [bpawn5.color,bpawn5.piece,bpawn5.x,bpawn5.y]=["b","Pawn",4,7]
    [bpawn6.color,bpawn6.piece,bpawn6.x,bpawn6.y]=["b","Pawn",3,7]
    [bpawn7.color,bpawn7.piece,bpawn7.x,bpawn7.y]=["b","Pawn",2,7]
    [bpawn8.color,bpawn8.piece,bpawn8.x,bpawn8.y]=["b","Pawn",1,7]
    [blrook.color,blrook.piece,blrook.x,blrook.y]=["b","Rook",8,8]
    [blknight.color,blknight.piece,blknight.x,blknight.y]=["b","Knight",7,8]
    [blbishop.color,blbishop.piece,blbishop.x,blbishop.y]=["b","Bishop",6,8]
    [brrook.color,brrook.piece,brrook.x,brrook.y]=["b","Rook",1,8]
    [brknight.color,brknight.piece,brknight.x,brknight.y]=["b","Knight",2,8]
    [brbishop.color,brbishop.piece,brbishop.x,brbishop.y]=["b","Bishop",3,8]
    [bqueen.color,bqueen.piece,bqueen.x,bqueen.y]=["b","Queen",4,8]
    [bking.color,bking.piece,bking.x,bking.y]=["b","King",5,8]
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
        elif xy in move(wpawn2): return True
        elif xy in move(wpawn3): return True
        elif xy in move(wpawn4): return True
        elif xy in move(wpawn5): return True
        elif xy in move(wpawn6): return True
        elif xy in move(wpawn7): return True
        elif xy in move(wpawn8): return True
        elif xy in move(wlrook): return True
        elif xy in move(wlknight): return True
        elif xy in move(wlbishop): return True
        elif xy in move(wrrook): return True
        elif xy in move(wrknight): return True
        elif xy in move(wrbishop): return True
        elif xy in move(wqueen): return True
        elif xy in move(wking): return True
        else: return False
    else:
        xy=[wking.x,wking.y]
        if xy in move(bpawn1): return True
        elif xy in move(bpawn2): return True
        elif xy in move(bpawn3): return True
        elif xy in move(bpawn4): return True
        elif xy in move(bpawn5): return True
        elif xy in move(bpawn6): return True
        elif xy in move(bpawn7): return True
        elif xy in move(bpawn8): return True
        elif xy in move(blrook): return True
        elif xy in move(blknight): return True
        elif xy in move(blbishop): return True
        elif xy in move(brrook): return True
        elif xy in move(brknight): return True
        elif xy in move(brbishop): return True
        elif xy in move(bqueen): return True
        elif xy in move(bking): return True
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
    elif piece=="tempwpawn1": return tempwpawn1
    elif piece=="tempwpawn2": return tempwpawn2
    elif piece=="tempwpawn3": return tempwpawn3
    elif piece=="tempwpawn4": return tempwpawn4
    elif piece=="tempwpawn5": return tempwpawn5
    elif piece=="tempwpawn6": return tempwpawn6
    elif piece=="tempwpawn7": return tempwpawn7
    elif piece=="tempwpawn8": return tempwpawn8
    elif piece=="tempwlrook": return tempwlrook
    elif piece=="tempwlknight": return tempwlknight
    elif piece=="tempwlbishop": return tempwlbishop
    elif piece=="tempwrrook": return tempwrrook
    elif piece=="tempwrknight": return tempwrknight
    elif piece=="tempwrbishop": return tempwrbishop
    elif piece=="tempwqueen": return tempwqueen
    elif piece=="tempwking": return tempwking
    elif piece=="tempbpawn1": return tempbpawn1
    elif piece=="tempbpawn2": return tempbpawn2
    elif piece=="tempbpawn3": return tempbpawn3
    elif piece=="tempbpawn4": return tempbpawn4
    elif piece=="tempbpawn5": return tempbpawn5
    elif piece=="tempbpawn6": return tempbpawn6
    elif piece=="tempbpawn7": return tempbpawn7
    elif piece=="tempbpawn8": return tempbpawn8
    elif piece=="tempblrook": return tempblrook
    elif piece=="tempblknight": return tempblknight
    elif piece=="tempblbishop": return tempblbishop
    elif piece=="tempbrrook": return tempbrrook
    elif piece=="tempbrknight": return tempbrknight
    elif piece=="tempbrbishop": return tempbrbishop
    elif piece=="tempbqueen": return tempbqueen
    elif piece=="tempbking": return tempbking
def checkcheck(piece,possible):
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking,tempwpawn1,tempwpawn2,tempwpawn3,tempwpawn4,tempwpawn5,tempwpawn6,tempwpawn7,tempwpawn8,tempwlrook,tempwlknight,tempwlbishop,tempwrrook,tempwrknight,tempwrbishop,tempwqueen,tempwking,tempbpawn1,tempbpawn2,tempbpawn3,tempbpawn4,tempbpawn5,tempbpawn6,tempbpawn7,tempbpawn8,tempblrook,tempblknight,tempblbishop,tempbrrook,tempbrknight,tempbrbishop,tempbqueen,tempbking
    for i in possible:
        clone()
        find(piece).x=i[0]
        find(piece).y=i[1]
        if check(i)!="none": find(check(i)).alive=False
        if kingcheck(find(piece).color): possible.remove(i)
        declone()
    return possible
def possiblePieces(color):
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking
    possible=[]
    if color=="w":
        if checkcheck("wpawn1",move(wpawn1)): possible.append("wpawn1")
        if checkcheck("wpawn2",move(wpawn2)): possible.append("wpawn2")
        if checkcheck("wpawn3",move(wpawn3)): possible.append("wpawn3")
        if checkcheck("wpawn4",move(wpawn4)): possible.append("wpawn4")
        if checkcheck("wpawn5",move(wpawn5)): possible.append("wpawn5")
        if checkcheck("wpawn6",move(wpawn6)): possible.append("wpawn6")
        if checkcheck("wpawn7",move(wpawn7)): possible.append("wpawn7")
        if checkcheck("wpawn8",move(wpawn8)): possible.append("wpawn8")
        if checkcheck("wlrook",move(wlrook)): possible.append("wlrook")
        if checkcheck("wlknight",move(wlknight)): possible.append("wlknight")
        if checkcheck("wlbishop",move(wlbishop)): possible.append("wlbishop")
        if checkcheck("wrrook",move(wrrook)): possible.append("wrrook")
        if checkcheck("wrknight",move(wrknight)): possible.append("wrknight")
        if checkcheck("wrbishop",move(wrbishop)): possible.append("wrbishop")
        if checkcheck("wqueen",move(wqueen)): possible.append("wqueen")
        if checkcheck("wking",move(wking)): possible.append("wking")
    else:
        if checkcheck("bpawn1",move(bpawn1)): possible.append("bpawn1")
        if checkcheck("bpawn2",move(bpawn2)): possible.append("bpawn2")
        if checkcheck("bpawn3",move(bpawn3)): possible.append("bpawn3")
        if checkcheck("bpawn4",move(bpawn4)): possible.append("bpawn4")
        if checkcheck("bpawn5",move(bpawn5)): possible.append("bpawn5")
        if checkcheck("bpawn6",move(bpawn6)): possible.append("bpawn6")
        if checkcheck("bpawn7",move(bpawn7)): possible.append("bpawn7")
        if checkcheck("bpawn8",move(bpawn8)): possible.append("bpawn8")
        if checkcheck("blrook",move(blrook)): possible.append("blrook")
        if checkcheck("blknight",move(blknight)): possible.append("blknight")
        if checkcheck("blbishop",move(blbishop)): possible.append("blbishop")
        if checkcheck("brrook",move(brrook)): possible.append("brrook")
        if checkcheck("brknight",move(brknight)): possible.append("brknight")
        if checkcheck("brbishop",move(brbishop)): possible.append("brbishop")
        if checkcheck("bqueen",move(bqueen)): possible.append("bqueen")
        if checkcheck("bking",move(bking)): possible.append("bking")
    return possible
def clone():
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking,tempwpawn1,tempwpawn2,tempwpawn3,tempwpawn4,tempwpawn5,tempwpawn6,tempwpawn7,tempwpawn8,tempwlrook,tempwlknight,tempwlbishop,tempwrrook,tempwrknight,tempwrbishop,tempwqueen,tempwking,tempbpawn1,tempbpawn2,tempbpawn3,tempbpawn4,tempbpawn5,tempbpawn6,tempbpawn7,tempbpawn8,tempblrook,tempblknight,tempblbishop,tempbrrook,tempbrknight,tempbrbishop,tempbqueen,tempbking
    for piece in ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8","wlrook","wlknight","wlbishop","wrrook","wrknight","wrbishop","wqueen","wking","bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8","blrook","blknight","blbishop","brrook","brknight","brbishop","bqueen","bking"]: [find("temp"+piece).color,find("temp"+piece).piece,find("temp"+piece).x,find("temp"+piece).y,find("temp"+piece).alive]=[find(piece).color,find(piece).piece,find(piece).x,find(piece).y,find(piece).alive]
def declone():
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking,tempwpawn1,tempwpawn2,tempwpawn3,tempwpawn4,tempwpawn5,tempwpawn6,tempwpawn7,tempwpawn8,tempwlrook,tempwlknight,tempwlbishop,tempwrrook,tempwrknight,tempwrbishop,tempwqueen,tempwking,tempbpawn1,tempbpawn2,tempbpawn3,tempbpawn4,tempbpawn5,tempbpawn6,tempbpawn7,tempbpawn8,tempblrook,tempblknight,tempblbishop,tempbrrook,tempbrknight,tempbrbishop,tempbqueen,tempbking
    for piece in ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8","wlrook","wlknight","wlbishop","wrrook","wrknight","wrbishop","wqueen","wking","bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8","blrook","blknight","blbishop","brrook","brknight","brbishop","bqueen","bking"]: [find(piece).color,find(piece).piece,find(piece).x,find(piece).y,find(piece).alive]=[find("temp"+piece).color,find("temp"+piece).piece,find("temp"+piece).x,find("temp"+piece).y,find("temp"+piece).alive]
def display():
    pass
    #♔♕♖♗♘♙♚♛♜♝♞♟︎
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
tempwpawn1=chess()
tempwpawn2=chess()
tempwpawn3=chess()
tempwpawn4=chess()
tempwpawn5=chess()
tempwpawn6=chess()
tempwpawn7=chess()
tempwpawn8=chess()
tempwlrook=chess()
tempwlknight=chess()
tempwlbishop=chess()
tempwrrook=chess()
tempwrknight=chess()
tempwrbishop=chess()
tempwqueen=chess()
tempwking=chess()
tempbpawn1=chess()
tempbpawn2=chess()
tempbpawn3=chess()
tempbpawn4=chess()
tempbpawn5=chess()
tempbpawn6=chess()
tempbpawn7=chess()
tempbpawn8=chess()
tempblrook=chess()
tempblknight=chess()
tempblbishop=chess()
tempbrrook=chess()
tempbrknight=chess()
tempbrbishop=chess()
tempbqueen=chess()
tempbking=chess()
reset()
color="w"
print("You can move the following pieces:",possiblePieces("w"))
d=input("What piece do you want to move? ")
possible=checkcheck(d,move(find(d)))
print("You can move",d,"from ["+str(find(d).x)+","+str(find(d).y)+"] to the following location(s):",possible)
print("Goodbye!")
