class chess:
    color="You're not suppossed to see this."
    piece="You're not suppossed to see this."
    x=0
    y=0
    hasMoved=False #this is just for pawns and castling but you could create custom pices with it.
    alive=True
    extra=False #can be used for special things like promoting pawns, en passant, or custom things. make it a list if you need more atributes
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
    ret="none"
    for piece in ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8","wlrook","wlknight","wlbishop","wrrook","wrknight","wrbishop","wqueen","wking","bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8","blrook","blknight","blbishop","brrook","brknight","brbishop","bqueen","bking"]:
        if xy==[find(piece).x,find(piece).y]and find(piece).alive: ret=piece
    return ret
def kingcheck(color):
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking
    ret=False
    if color=="b":
        xy=[bking.x,bking.y]
        for piece in ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8","wlrook","wlknight","wlbishop","wrrook","wrknight","wrbishop","wqueen","wking"]:
            if xy in move(find(piece)): ret=True
    else:
        xy=[wking.x,wking.y]
        for piece in ["bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8","blrook","blknight","blbishop","brrook","brknight","brbishop","bqueen","bking"]:
            if xy in move(find(piece)): ret=True
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
        if check(i)!=["none"]: find(check(i)).alive=False
        if kingcheck(find(piece).color): possible.remove(i)
        declone()
    return possible
def possiblePieces(color):
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking
    possible=["none"]
    if color=="w":
        for piece in ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8","wlrook","wlknight","wlbishop","wrrook","wrknight","wrbishop","wqueen","wking"]:
            if checkcheck(piece,move(find(piece))): possible.append(piece)
    else:
        for piece in ["bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8","blrook","blknight","blbishop","brrook","brknight","brbishop","bqueen","bking"]:
            if checkcheck(piece,move(find(piece))): possible.append(piece)
    if len(possible)>1:possible.remove("none")
    return possible
def clone():
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking,tempwpawn1,tempwpawn2,tempwpawn3,tempwpawn4,tempwpawn5,tempwpawn6,tempwpawn7,tempwpawn8,tempwlrook,tempwlknight,tempwlbishop,tempwrrook,tempwrknight,tempwrbishop,tempwqueen,tempwking,tempbpawn1,tempbpawn2,tempbpawn3,tempbpawn4,tempbpawn5,tempbpawn6,tempbpawn7,tempbpawn8,tempblrook,tempblknight,tempblbishop,tempbrrook,tempbrknight,tempbrbishop,tempbqueen,tempbking
    for piece in ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8","wlrook","wlknight","wlbishop","wrrook","wrknight","wrbishop","wqueen","wking","bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8","blrook","blknight","blbishop","brrook","brknight","brbishop","bqueen","bking"]: [find("temp"+piece).color,find("temp"+piece).piece,find("temp"+piece).x,find("temp"+piece).y,find("temp"+piece).alive,find("temp"+piece).hasMoved,find("temp"+piece).extra]=[find(piece).color,find(piece).piece,find(piece).x,find(piece).y,find(piece).alive,find(piece).hasMoved,find(piece).extra]
def declone():
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking,tempwpawn1,tempwpawn2,tempwpawn3,tempwpawn4,tempwpawn5,tempwpawn6,tempwpawn7,tempwpawn8,tempwlrook,tempwlknight,tempwlbishop,tempwrrook,tempwrknight,tempwrbishop,tempwqueen,tempwking,tempbpawn1,tempbpawn2,tempbpawn3,tempbpawn4,tempbpawn5,tempbpawn6,tempbpawn7,tempbpawn8,tempblrook,tempblknight,tempblbishop,tempbrrook,tempbrknight,tempbrbishop,tempbqueen,tempbking
    for piece in ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8","wlrook","wlknight","wlbishop","wrrook","wrknight","wrbishop","wqueen","wking","bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8","blrook","blknight","blbishop","brrook","brknight","brbishop","bqueen","bking"]: [find(piece).color,find(piece).piece,find(piece).x,find(piece).y,find(piece).alive,find(piece).hasMoved,find(piece).extra]=[find("temp"+piece).color,find("temp"+piece).piece,find("temp"+piece).x,find("temp"+piece).y,find("temp"+piece).alive,find("temp"+piece).hasMoved,find("temp"+piece).extra]
def translateMoveMade(moveMade):
    if isinstance(moveMade[1],int): moveMade=["A","B","C","D","E","F","G","H"][moveMade[0]-1]+str(moveMade[1])
    else: moveMade=[["A","B","C","D","E","F","G","H"].index(moveMade[0]+1),int(moveMade[1])]
    return moveMade
def display():
    global wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,wlrook,wlknight,wlbishop,wrrook,wrknight,wrbishop,wqueen,wking,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8,blrook,blknight,blbishop,brrook,brknight,brbishop,bqueen,bking
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
play="y"
while play=="y" or play=="Y":
    color="w"
    reset()
    while True:
        if possiblePieces(color)==["none"]:
            if kingcheck(color): print("The",color,"player is in checkmate!")
            else: print("Stalemate!")
            print("The",swap(color,"w","b"),"player wins!")
        print("You can move the following pieces:",possiblePieces(color)) #add a user frendly print function
        pieceMoveMade=input("What piece do you want to move? ") #make a loop that rejects invalid inputs
        while True:
            moveMade=translateMoveMade(input("Where do you want to move "+pieceMoveMade+"? "))
            if moveMade not in move(find(pieceMoveMade)):
                print("That's not a vlaid move!")
                continue
            elif moveMade not in checkcheck(pieceMoveMade,move(find(pieceMoveMade))):
                print("That would put your king in check!")
                continue
            else: 
                print(pieceMoveMade,"moved to",translateMoveMade(moveMade))
                break
        [find(pieceMoveMade).x,find(pieceMoveMade).y]=moveMade
        find(pieceMoveMade).hasMoved=True
        if check(moveMade)!=["none"]: find(check(moveMade)).alive=False
        if find(pieceMoveMade).piece=="Pawn" and moveMade[1]==8+(colorrev(find(pieceMoveMade).color,3.5)-3.5):
            find(pieceMoveMade).piece="Queen" #add a choice
        #set extra in every pawn to false. if true they can be captured via en passant
        display()
        color=swap(color,"w","b")
        if kingcheck(color): print("The",color,"player is in check.")
    play=input("Do you want to play again? (Y/N) ")
print("Goodbye!")
