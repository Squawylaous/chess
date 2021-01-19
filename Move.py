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
        elif piece.piece="Teleporter":
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False,canJump=True,canCapture=False)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,canJump=True,canCapture=False)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,canJump=True,canCapture=False)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False,1,1,mustCapture=True)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,1,1,mustCapture=True)
            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,1,1,mustCapture=True)
    return possible
