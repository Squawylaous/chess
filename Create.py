print("class chess:\n    name=\"You're not suppossed to see this.\"\n    color=\"You're not suppossed to see this.\"\n    piece=\"You're not suppossed to see this.\"\n    x=0\n    y=0\n    hasMoved=False\n    alive=True\n    extra=False\n    displayName=\"You're not suppossed to see this.\"\n    tempcolor=\"You're not suppossed to see this.\"\n    temppiece=\"You're not suppossed to see this.\"\n    tempx=0\n    tempy=0\n    temphasMoved=False\n    tempalive=True\n    tempextra=False\n    tempdisplayName=\"You're not suppossed to see this.\"\n    def reset(self,color,piece,displayName,x,y,alive=True,hasMoved=False,extra=False):\n        self.color=color\n        self.piece=piece\n        self.x=x\n        self.y=y\n        self.hasMoved=hasMoved\n        self.alive=alive\n        self.extra=extra\n        self.displayName=displayName\n        num=0\n        for pieces in allPieces:\n            if allPieces.piece==piece: num+=1\n        self.name=color+piece.lower()+str(num)\n        self.clone()\n    def clone(piece): [piece.tempcolor,piece.temppiece,piece.tempx,piece.tempy,piece.tempalive,piece.temphasMoved,piece.tempextra,piece.tempdisplayName]=[piece.color,piece.piece,piece.x,piece.y,piece.alive,piece.hasMoved,piece.extra,piece.displayName]\n    def declone(piece): [piece.color,piece.piece,piece.x,piece.y,piece.alive,piece.hasMoved,piece.extra,piece.displayName]=[piece.tempcolor,piece.temppiece,piece.tempx,piece.tempy,piece.tempalive,piece.temphasMoved,piece.tempextra,piece.tempdisplayName]\ndef fill(x,y): return str(x)+(\" \"*(y-len(str(x))))\ndef intToAlphabet(x):\n    alpha=[\"A\",\"B\",\"C\",\"D\",\"E\",\"F\",\"G\",\"H\",\"I\",\"J\",\"K\",\"L\",\"M\",\"N\",\"O\",\"P\",\"Q\",\"R\",\"S\",\"T\",\"U\",\"V\",\"W\",\"X\",\"Y\",\"Z\"]\n    ret=\"\"\n    place=0\n    y=0\n    while y<x:\n        place+=1\n        y=0\n        for w in range(place): y+=(26**(w+1))\n    for i in range(place-1,0,-1):\n        if x//(26**i)==27:\n            ret+=\"Z\"\n            x=(x%(26**i))+26\n        else:\n            ret+=alpha[x//(26**i)-1]\n            x%=26**i\n    ret+=alpha[x-1]\n    return ret\ndef alphabetToInt(y):\n    alpha=[\"A\",\"B\",\"C\",\"D\",\"E\",\"F\",\"G\",\"H\",\"I\",\"J\",\"K\",\"L\",\"M\",\"N\",\"O\",\"P\",\"Q\",\"R\",\"S\",\"T\",\"U\",\"V\",\"W\",\"X\",\"Y\",\"Z\"]\n    ret=0\n    x=\"\"\n    for i in range(len(y)): x=y[i]+x\n    for i in range(len(x)):\n        ret+=(26**i)*(alpha.index(x[i])+1)\n    return ret\ndef swap(swap,x,y):\n    if swap==x: return y\n    if swap==y: return x\ndef pos(piece,x,y): [piece.x,piece.y]=[x,y]\ndef colorrev(color,x):\n    if color==\"w\": return x\n    else: return -x\ndef check(xy):\n    global allPieces\n    ret=\"none\"\n    for piece in allPieces:\n        if xy==[piece.x,piece.y] and piece.alive: ret=piece\n    return ret\ndef kingcheck(color):\n    global allPieces\n    ret=False\n    kings=[]\n    for piece in allPieces:\n        if piece.piece==\"King\" and piece.color=color: kings.append(piece)\n    for king in kings:\n        for piece in allPieces:\n            if piece.piece==\"King\": break\n            elif [king.x,king.y] in move(piece): ret=True\n    return ret\ndef moveto(x,y,color,canCapture=True,mustCapture=False):\n    piece=check([x,y])\n    if (piece==\"none\" and not mustCapture): return True\n    elif not isinstance(piece,str):\n        if (piece.color!=color and canCapture): return True \n    else: return False\ndef linearmoveto(possible,x,y,color,acrossx,acrossy,xlimit=False,ylimit=False,xdirec=0,ydirec=0,xmin=1,ymin=1,xmult=1,ymult=1,canJump=False,canCapture=True,mustCapture=False):\n    global board\n    if not isinstance(xlimit,bool):\n        xplim=x+xlimit+1\n        xnlim=x-xlimit-1\n        if xplim>board[0]+1: xplim=board[0]+1\n        if xnlim<0: xnlim=0\n    else:\n        xplim=board[0]+1\n        xnlim=0\n    if not isinstance(ylimit,bool):\n        yplim=y+ylimit+1\n        ynlim=y-ylimit-1\n        if yplim>board[1]+1: yplim=board[1]+1\n        if ynlim<0: ynlim=0\n    else:\n        yplim=board[1]+1\n        ynlim=0\n    xdirec=colorrev(color,xdirec)\n    ydirec=colorrev(color,ydirec)\n    if acrossx and not acrossy:\n        if xdirec>=0:\n            for i in range(x+xmult,xplim,xmult):\n                if moveto(i,y,color,canCapture,mustCapture):\n                    if i>=x+xmin: possible.append([i,y])\n                    if check([i,y])!=\"none\":\n                        if not canJump: break\n                elif not canJump: break\n        if xdirec<=0:\n            for i in range(x-xmult,xnlim,-xmult):\n                if moveto(i,y,color,canCapture,mustCapture):\n                    if i<=x-xmin: possible.append([i,y])\n                    if check([i,y])!=\"none\":\n                        if not canJump: break\n                elif not canJump: break\n    if acrossy and not acrossx:\n        if ydirec>=0:\n            for i in range(y+ymult,yplim,ymult):\n                if moveto(x,i,color,canCapture,mustCapture):\n                    if i>=y+ymin: possible.append([x,i])\n                    if check([x,i])!=\"none\":\n                        if not canJump: break\n                elif not canJump: break\n        if ydirec<=0:\n            for i in range(y-ymult,ynlim,-ymult):\n                if moveto(x,i,color,canCapture,mustCapture):\n                    if i<=y-ymin: possible.append([x,i])\n                    if check([x,i])!=\"none\":\n                        if not canJump: break\n                elif not canJump: break\n    if acrossx and acrossy:\n        if ydirec>=0:\n            if xdirec>=0:\n                j=y+ymult\n                for i in range(x+xmult,xplim,xmult):\n                    if j>=yplim: break\n                    if moveto(i,j,color,canCapture,mustCapture):\n                        if i>=x+xmult and j>=y+ymin: possible.append([i,j])\n                        if check([i,j])!=\"none\":\n                            if not canJump: break\n                    elif not canJump: break\n                    j+=ymult\n            if xdirec<=0:\n                j=y+ymult\n                for i in range(x-xmult,xnlim,-xmult):\n                    if j>=yplim: break\n                    if moveto(i,j,color,canCapture,mustCapture):\n                        if i<=x-xmin and j>=y+ymin: possible.append([i,j])\n                        if check([i,j])!=\"none\":\n                            if not canJump: break\n                    elif not canJump: break\n                    j+=ymult\n        if ydirec>=0:\n            if xdirec>=0:\n                j=y-ymult\n                for i in range(x+xmult,xplim,xmult):\n                    if j<=ynlim: break\n                    if moveto(i,j,color,canCapture,mustCapture):\n                        if i>=x+xmin and j<=y-ymin: possible.append([i,j])\n                        if check([i,j])!=\"none\":\n                            if not canJump: break\n                    elif not canJump: break\n                    j-=ymult\n            if xdirec<=0:\n                j=y-ymult\n                for i in range(x-xmult,xnlim,-xmult):\n                    if j<=ynlim: break\n                    if moveto(i,j,color,canCapture,mustCapture):\n                        if i<=x-xmin and j<=y-ymin: possible.append([i,j])\n                        if check([i,j])!=\"none\":\n                            if not canJump: break\n                    elif not canJump: break\n                    j-=ymult\n    return possible\ndef checkcheck(piece,possible):\n    global allPieces,board\n    if possible==[]: possible=\"none\"\n    else:\n        for pieces in allPieces: pieces.clone()\n        for i in possible:\n            if check(i)!=\"none\": check(i).alive=False\n            piece.x=i[0]\n            piece.y=i[1]\n            if kingcheck(piece.color): possible.remove(i)\n            elif i[0]<1 or i[0]>board[0] or i[1]<1 or i[1]>board[1]: possible.remove(i)\n        for pieces in allPieces: pieces.declone()\n    if possible==[]: possible=\"none\"\n    return possible\ndef possiblePieces(color):\n    global allPieces\n    possible=[\"none\"]\n    if color==\"w\":\n        for piece in allPieces:\n      pieces=checkcheck(piece,move(piece))\n            if piece.color==\"w\" and pieces!=\"none\": possible.append(piece)\n    else:\n        for piece in allPieces:\n            pieces=checkcheck(piece,move(piece))\n            if piece.color==\"b\" and pieces!=\"none\": possible.append(piece)\n    if len(possible)>1:possible.remove(\"none\")\n    return possible\ndef translateMoveMade(moveMade):\n    if isinstance(moveMade[0],int): moveMade=intToAlphabet(moveMade[0])+\"\"+str(moveMade[1])\n    else:\n        for char in range(len(moveMade)):\n            if moveMade[char].isdigit(): charindex=char\n        moveMade=[alphabetToInt(moveMade[:charindex]),int(moveMade[charindex:])]\n    return moveMade\ndef translatePossiblePieces(possiblePieces):\n    ret=\"\"\n    for piece in range(len(possiblePieces)):\n        ret+=possiblePieces[piece].piece+\" \"\n        for char in possiblePieces[piece].name:\n            if char.isdigit(): ret+=char\n        ret+=\" (\"+translateMoveMade([possiblePieces[piece].x,possiblePieces[piece].y])+\"), \"\n    return ret[:-2]\ndef display():\n    global board\n    print(\"   ┌───\"+\"┬───\"*(board[0]-1)+\"┐\")\n    for y in range(board[1],0,-1):\n        print(\" \",end=fill(y,2))\n        for x in range(1,board[0]+1):\n            print(end=\"│ \")\n            piece=check([x,y])\n            if piece!=\"none\":\n                if piece.alive:\n                    if piece.color==\"w\": color=\"\033[33m\"\n                    else: color=\"\033[31m\"\n                    name=color+piece.displayName\n                else: name=\" \"\n            else: name=\" \"\n            print(name,end=\"\033[m\")\n            print(end=\" \")\n        print(\"│\")\n        if y!=1: print(\"   ├───\"+\"┼───\"*(board[0]-1)+\"┤\")\n        else: continue\n    print(\"   └───\"+\"┴───\"*(board[0]-1)+\"┘\")\n    print(end=\"  \")\n    for x in range(1,board[0]+1): print(\"   \",end=intToAlphabet(x))\n    print(\"\")\n"+
    "def move(piece):\n    global board\n    possible=[]\n    if piece.alive:\n        if piece.piece==\"King\":\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False,1,1)\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,1,1)\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,1,1)\n            for i in range(piece.x-1,0,-1):\n                check=check([i,piece.y])\n                if check!=\"none\":\n                    if check.piece!=\"Rook\" or check.color!=piece.color or check.hasMoved:\n                        break\n                    clone()\n                    piece.x-=1\n                    if not kingcheck(piece.color): possible.append([piece.x-2,piece.y])\n                    declone()\n            for i in range(piece.x+1,0,+1):\n                check=check([i,piece.y])\n                if check!=\"none\":\n                    if check.piece!=\"Rook\" or check.color!=piece.color or check.hasMoved:\n                        break\n                    clone()\n                    piece.x+=1\n                    if not kingcheck(piece.color): possible.append([piece.x+2,piece.y])\n                    declone()\n        elif piece.piece==\"Pawn\":\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,0,1,ydirec=1,canCapture=False)\n            if not piece.hasMoved: possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True,0,2,ydirec=1,ymin=2,canCapture=False)\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,1,1,ydirec=1,mustCapture=True)\n            temp=check([piece.x+1,piece.y])\n            if temp!=\"none\":\n                if temp.piece==\"Pawn\" and temp.color!=piece.color and temp.extra and moveto(piece.x+1,piece.y+colorrev(piece.color,1),piece.color,False): possible.append([piece.x+1,piece.y+colorrev(piece.color,1)])\n            temp=check([piece.x-1,piece.y])\n            if temp!=\"none\":\n                if temp.piece==\"Pawn\" and temp.color!=piece.color and temp.extra and moveto(piece.x-1,piece.y+colorrev(piece.color,1),piece.color,False): possible.append([piece.x-1,piece.y+colorrev(piece.color,1)])\n        elif piece.piece==\"Rook\":\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False)\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True)\n        elif piece.piece==\"Knight\":\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,2,1,xmult=2)\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True,1,2,ymult=2)\n        elif piece.piece==\"Bishop\":\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True)\n        elif piece.piece==\"Queen\":\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,False)\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,False,True)\n            possible=linearmoveto(possible,piece.x,piece.y,piece.color,True,True)\n    return possible\n"+
    "def reset():\n    global allPieces\n    for i in range(8):\n        allPieces[i].reset(\"w\",\"Pawn\",\"P\",i+1,2)\n        allPieces[8+i].reset(\"b\",\"Pawn\",\"p\",i+1,7)\n    allPieces[16].reset(\"w\",\"Rook\",\"R\",1,1)\n    allPieces[17].reset(\"w\",\"Rook\",\"R\",8,1)\n    allPieces[18].reset(\"b\",\"Rook\",\"R\",8,8)\n    allPieces[19].reset(\"b\",\"Rook\",\"R\",1,8)\n    allPieces[20].reset(\"w\",\"Knight\",\"N\",2,1)\n    allPieces[21].reset(\"w\",\"Knight\",\"N\",7,1)\n    allPieces[22].reset(\"b\",\"Knight\",\"N\",7,8)\n    allPieces[23].reset(\"b\",\"Knight\",\"N\",2,8)\n    allPieces[24].reset(\"w\",\"Bishop\",\"B\",3,1)\n    allPieces[25].reset(\"w\",\"Bishop\",\"B\",6,1)\n    allPieces[26].reset(\"b\",\"Bishop\",\"B\",6,8)\n    allPieces[27].reset(\"b\",\"Bishop\",\"B\",3,8)\n    allPieces[28].reset(\"w\",\"Queen\",\"Q\",4,1)\n    allPieces[29].reset(\"b\",\"Queen\",\"Q\",4,8)\n    allPieces[30].reset(\"w\",\"King\",\"K\",5,1)\n    allPieces[31].reset(\"b\",\"King\",\"K\",5,8)\nallPieces=[chess() for i in range(32)]\nboard=[8,8]"+
    "\nplay=\"y\"\nwhile play==\"y\" or play==\"Y\":\n    color=\"w\"\n    reset()\n    while True:\n        if color==\"w\": displayColor=\"White\"\n        else: displayColor=\"Black\"\n        display()\n        if possiblePieces(color)==[\"none\"]:\n            if kingcheck(color): print(\"The\",displayColor,\"player is in checkmate!\")\n            else:\n                for piece in allPieces:\n                    if piece.color==color and piece.alive:\n                        print(\"Stalemate!\")\n                        noPieces=False\n                        break\n                    else: noPieces=True\n                if noPieces: print(\"The\",displayColor,\"player is out of pieces!\")\n            print(\"The\",swap(displayColor,\"White\",\"Black\"),\"player wins!\")\n            break\n        print(\"The\",displayColor,\"player can move the following pieces:\",translatePossiblePieces(possiblePieces(color)))\n        while True:\n            pieceMoveMade=(input(\"What piece do you want to move? \").replace(\" \",\"\")).lower()\n            for piece in allPieces:\n                if pieceMoveMade==piece.name and piece.color==color:\n                    pieceMoveMade=piece\n                    break\n                else: pieceMoveMade=\"none\"\n            if pieceMoveMade!=\"none\":\n                if pieceMoveMade in possiblePieces(color): break\n                else: print(\"You can't move that piece!\")\n            else: print(\"That is not a valid piece!\")\n        while True:\n            pieceMoveMadeMoves=move(pieceMoveMade)\n            try: moveMade=translateMoveMade(input(\"Where do you want to move \"+translatePossiblePieces([pieceMoveMade])+\"? \").upper())\n            except:\n                print(\"That's not a vlaid move!\")\n                continue\n            if moveMade not in pieceMoveMadeMoves:\n                print(\"That's not a vlaid move!\")\n                continue\n            elif moveMade not in checkcheck(pieceMoveMade,pieceMoveMadeMoves):\n                print(\"That would put your king in check!\")\n                continue\n            else: \n                print(translatePossiblePieces([pieceMoveMade]),\"moved to\",translateMoveMade(moveMade))\n                break\n        if pieceMoveMade.piece==\"King\": pieceMoveMade.tempx=pieceMoveMade.x\n        if check(moveMade)!=\"none\": check(moveMade).alive=False\n        [pieceMoveMade.x,pieceMoveMade.y]=moveMade\n        "+
    "if pieceMoveMade.piece==\"Pawn\":\n            if moveMade[1]==board[0]+(colorrev(pieceMoveMade.color,(board[0]-1)/2)-((board[0]-1)/2)):\n                pawnPromote=input(\"What do you want to promote your pawn to?\").capatlize()\n                while pawnPromote not in [\"Queen\",\"Rook\",\"Bishop\",\"Knight\"]:\n                    print(\"That's not a valid piece!\")\n                    pawnPromote=input(\"What do you want to promote your pawn to?\").capatlize()\n                count=1\n                for piece in allPieces:\n                    if piece.piece==pawnPromote: count+=1\n                pieceMoveMade.piece=pawnPromote\n                pieceMoveMade.name=pawnPromote.lower()+str(count)\n                if pawnPromote==\"Knight\": pieceMoveMade.displayName=\"N\"\n                else: pieceMoveMade.displayName=pawnPromote[0]\n            enPassant=check([pieceMoveMade.x,pieceMoveMade.y-colorrev(pieceMoveMade.color,1)])\n            if enPassant!=\"none\":\n                if enPassant.extra and enPassant.color!=pieceMoveMade.color: enPassant.alive=False\n        if pieceMoveMade.piece==\"King\":\n            if abs(pieceMoveMade.tempx-pieceMoveMade.x)==2:\n                if pieceMoveMade.tempx>pieceMoveMade.x: diff=-1\n                else: diff=1\n                for i in range(pieceMoveMade.tempx+diff,0,diff):\n                    check=check([i,pieceMoveMade.y])\n                    if check.piece==\"Rook\":\n                        check.x=pieceMoveMade.x-diff\n        for piece in allPieces:\n            if piece.piece==\"Pawn\": pieceMoveMade.extra=False\n        if not pieceMoveMade.hasMoved and pieceMoveMade.piece==\"Pawn\": pieceMoveMade.extra=True"+
    "\n        pieceMoveMade.hasMoved=True\n        color=swap(color,\"w\",\"b\")\n        if kingcheck(color): print(\"The\",swap(displayColor,\"White\",\"Black\"),\"player is in check.\")\n    play=input(\"Do you want to play again? (Y/N) \")\nprint(\"Goodbye!\")")
