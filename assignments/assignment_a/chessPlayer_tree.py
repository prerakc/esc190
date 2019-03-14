def GetPlayerPositions(board,player):
   W = 10
   B = 20
   x0=zip(board,range(0,64,1))
   x1=filter(lambda x : ((x[0]-player) < W) and ((x[0]-player) >= 0), x0)
   return map(lambda x:x[1],x1)

def GetPieceLegalMoves(board, pos):
   piece = board[pos]
   accum = []
   if piece != 0:
      if piece % 10 == 0:
         accum = GenPawnMoves(board, pos)
      elif piece % 10 == 1:
         accum = GenKnightMoves(board, pos)
      elif piece % 10 == 2:
         accum = GenBishopMoves(board, pos)
      elif piece % 10 == 3:
         accum = GenRookMoves(board, pos)
      elif piece % 10 == 4:
         accum = GenQueenMoves(board, pos)
      elif piece % 10 == 5:
         accum = GenKingMoves(board, pos)
   return accum

'''
def GenPawnMoves(board,pos):
   accum = []
   piece = board[pos]
   rowmove = 0
   if piece >= 20:
      rowmove = -8
   elif piece >= 10 and piece < 20:
      rowmove = 8
   if (pos >= 8) and (pos <= 55):
      if board[pos+rowmove] == 0:
         accum += [pos+rowmove]
      if (pos % 8 != 0):
         if (rowmove == -8 and board[pos+rowmove-1] >= 10 and board[pos+rowmove-1] < 20) or (rowmove == 8 and board[pos+rowmove-1] >= 20):
            accum += [pos+rowmove-1]
      if (pos % 8 != 7):
         if (rowmove == -8 and board[pos+rowmove+1] >= 10 and board[pos+rowmove+1] < 20) or (rowmove == 8 and board[pos+rowmove+1] >= 20):
            accum += [pos+rowmove+1]
   return accum

def GenPawnMoves(board,pos):
   #Create list for possible moves and determine where pawn can move
   accum = []
   offsets = [7,8,9]
   if board[pos] == 20:
      offsets = [i * -1 for i in offsets]

   #Generate possible moves
   for i in offsets:
      newpos = pos+i
      #Make sure new position lies on board
      if IsOnBoard(newpos):
         move = canMove(board,pos,newpos) 
         
         #Checking in front of pawn
         if (i == 8) or (i == -8):
            #Empty tile
            if (move == 0):
               accum += [newpos]

         #Checking pawn's frontal diagonals
         if ((i == 9) or (i == -7)) and (pos % 8 != 7):
            #Enemy occupied
             if (move == -1):
                accum += [newpos]
         #Checking pawn's frontal diagonals
         if ((i == 7) or (i == -9)) and (pos % 8 != 0):
            #Enemy occupied
            if (move == -1):
               accum += [newpos]
  
   #Return possible moves
   return accum

def GenBishopMoves(board,pos):
   accum = []
   piece = board[pos]
   moveRight = 7-pos%8
   moveLeft = pos%8
   moveUp = int(pos / 8)
   moveDown = 7 - int(pos / 8)
   if piece >= 20:
      for i in range(1,min(moveRight,moveUp)+1,1):
         if (board[pos-8*i+i] == 0) or (board[pos-8*i+i] >= 10 and board[pos-8*i+i] < 20):
            accum += [pos-8*i+i]
         if (board[pos-8*i+i] >= 20) or (board[pos-8*i+i] >= 10 and board[pos-8*i+i] < 20):
            break
      for i in range(1,min(moveRight,moveDown)+1,1):
         if (board[pos+8*i+i] == 0) or (board[pos+8*i+i] >= 10 and board[pos+8*i+i] < 20):
            accum += [pos+8*i+i]
         if (board[pos+8*i+i] >= 20) or (board[pos+8*i+i] >= 10 and board[pos+8*i+i] < 20):
            break
      for i in range(1,min(moveLeft,moveUp)+1,1):
         if (board[pos-8*i-i] == 0) or (board[pos-8*i-i] >= 10 and board[pos-8*i-i] < 20):
            accum += [pos-8*i-i]
         if (board[pos-8*i-i] >= 20) or (board[pos-8*i-i] >= 10 and board[pos-8*i-i] < 20):
            break
      for i in range(1,min(moveLeft,moveDown)+1,1):
         if (board[pos+8*i-i] == 0) or (board[pos+8*i-i] >= 10 and board[pos+8*i-i] < 20):
            accum += [pos+8*i-i]
         if (board[pos+8*i-i] >= 20) or (board[pos+8*i-i] >= 10 and board[pos+8*i-i] < 20):
            break
   elif piece >= 10 and piece < 20:
      for i in range(1,min(moveRight,moveUp)+1,1):
         if (board[pos-8*i+i] == 0) or (board[pos-8*i+i] >= 20):
            accum += [pos-8*i+i]
         if (board[pos-8*i+i] >= 20) or (board[pos-8*i+i] >= 10 and board[pos-8*i+i] < 20):
            break
      for i in range(1,min(moveRight,moveDown)+1,1):
         if (board[pos+8*i+i] == 0) or (board[pos+8*i+i] >= 20):
            accum += [pos+8*i+i]
         if (board[pos+8*i+i] >= 20) or (board[pos+8*i+i] >= 10 and board[pos+8*i+i] < 20):
            break
      for i in range(1,min(moveLeft,moveUp)+1,1):
         if (board[pos-8*i-i] == 0) or (board[pos-8*i-i] >= 20):
            accum += [pos-8*i-i]
         if (board[pos-8*i-i] >= 20) or (board[pos-8*i-i] >= 10 and board[pos-8*i-i] < 20):
            break
      for i in range(1,min(moveLeft,moveDown)+1,1):
         if (board[pos+8*i-i] == 0) or (board[pos+8*i-i] >= 20):
            accum += [pos+8*i-i]
         if (board[pos+8*i-i] >= 20) or (board[pos+8*i-i] >= 10 and board[pos+8*i-i] < 20):
            break
   return accum

def GenRookMoves(board,pos):
   accum = []
   piece = board[pos]
   moveRight = 7-pos%8
   moveLeft = pos%8
   moveUp = int(pos / 8)
   moveDown = 7 - int(pos / 8)
   if piece >= 20:
      for i in range(1,moveRight+1,1):
         if (board[pos+i] == 0) or (board[pos+i] >= 10 and board[pos+i] < 20):
            accum += [pos+i]
         if (board[pos+i] >= 20) or (board[pos+i] >= 10 and board[pos+i] < 20):
            break
      for i in range(1,moveLeft+1,1):
         if (board[pos-i] == 0) or (board[pos-i] >= 10 and board[pos-i] < 20):
            accum += [pos-i]
         if (board[pos-i] >= 20) or (board[pos-i] >= 10 and board[pos-i] < 20):
            break
      for i in range(1,moveDown+1,1):
         if (board[pos+8*i] == 0) or (board[pos+8*i] >= 10 and board[pos+8*i] < 20):
            accum += [pos+8*i]
         if (board[pos+8*i] >= 20) or (board[pos+8*i] >= 10 and board[pos+8*i] < 20):
            break
      for i in range(1,moveUp+1,1):
         if (board[pos-8*i] == 0) or (board[pos-8*i] >= 10 and board[pos-8*i] < 20):
            accum += [pos-8*i]
         if (board[pos-8*i] >= 20) or (board[pos-8*i] >= 10 and board[pos-8*i] < 20):
            break
   elif piece >= 10 and piece < 20:
      for i in range(1,moveRight+1,1):
         if (board[pos+i] == 0) or (board[pos+i] >= 20):
            accum += [pos+i]
         if (board[pos+i] >= 20) or (board[pos+i] >= 10 and board[pos+i] < 20):
            break
      for i in range(1,moveLeft+1,1):
         if (board[pos-i] == 0) or (board[pos-i] >= 20):
            accum += [pos-i]
         if (board[pos-i] >= 20) or (board[pos-i] >= 10 and board[pos-i] < 20):
            break
      for i in range(1,moveDown+1,1):
         if (board[pos+8*i] == 0) or (board[pos+8*i] >= 20):
            accum += [pos+8*i]
         if (board[pos+8*i] >= 20) or (board[pos+8*i] >= 10 and board[pos+8*i] < 20):
            break
      for i in range(1,moveUp+1,1):
         if (board[pos-8*i] == 0) or (board[pos-8*i] >= 20):
            accum += [pos-8*i]
         if (board[pos-8*i] >= 20) or (board[pos-8*i] >= 10 and board[pos-8*i] < 20):
            break
   return accum

def GenQueenMoves(board,pos):
   accum = []
   accum += GenRookMoves(board,pos)
   accum += GenBishopMoves(board,pos)
   return accum

def GenKingMoves(board,pos):
   accum = []
   piece = board[pos]
   moveRight = 1
   moveLeft = 1
   moveUp = 1
   moveDown = 1
   if pos % 8 == 7:
      moveRight = 0
   if pos % 8 == 0:
      moveLeft = 0
   if int(pos / 8) == 0:
      moveUp = 0
   if int(pos / 8) == 7:
      moveDown = 0
   if piece >= 20:
      if moveRight ==  1:
         if (board[pos+1] == 0) or (board[pos+1] >= 10 and board[pos+1] < 20):
            accum += [pos+1]
      if moveLeft == 1:
         if (board[pos-1] == 0) or (board[pos-1] >= 10 and board[pos-1] < 20):
            accum += [pos-1]
      if moveDown == 1:
         if (board[pos+8] == 0) or (board[pos+8] >= 10 and board[pos+8] < 20):
            accum += [pos+8]
      if moveUp == 1:
         if (board[pos-8] == 0) or (board[pos-8] >= 10 and board[pos-8] < 20):
            accum += [pos-8]
      if min(moveRight,moveUp) == 1:
         if (board[pos-8+1] == 0) or (board[pos-8+1] >= 10 and board[pos-8+1] < 20):
            accum += [pos-8+1]
      if min(moveRight,moveDown) == 1:
         if (board[pos+8+1] == 0) or (board[pos+8+1] >= 10 and board[pos+8+1] < 20):
            accum += [pos+8+1]
      if min(moveLeft,moveUp) == 1:
         if (board[pos-8-1] == 0) or (board[pos-8-1] >= 10 and board[pos-8-1] < 20):
            accum += [pos-8-1]
      if min(moveLeft,moveDown) == 1:
         if (board[pos+8-1] == 0) or (board[pos+8-1] >= 10 and board[pos+8-1] < 20):
            accum += [pos+8-1]
   elif piece >= 10 and piece < 20:
      if moveRight ==  1:
         if (board[pos+1] == 0) or (board[pos+1] >= 20):
            accum += [pos+1]
      if moveLeft == 1:
         if (board[pos-1] == 0) or (board[pos-1] >= 20):
            accum += [pos-1]
      if moveDown == 1:
         if (board[pos+8] == 0) or (board[pos+8] >= 20):
            accum += [pos+8]
      if moveUp == 1:
         if (board[pos-8] == 0) or (board[pos-8] >= 20):
            accum += [pos-8]
      if min(moveRight,moveUp) == 1:
         if (board[pos-8+1] == 0) or (board[pos-8+1] >= 20):
            accum += [pos-8+1]
      if min(moveRight,moveDown) == 1:
         if (board[pos+8+1] == 0) or (board[pos+8+1] >= 20):
            accum += [pos+8+1]
      if min(moveLeft,moveUp) == 1:
         if (board[pos-8-1] == 0) or (board[pos-8-1] >= 20):
            accum += [pos-8-1]
      if min(moveLeft,moveDown) == 1:
         if (board[pos+8-1] == 0) or (board[pos+8-1] >= 20):
            accum += [pos+8-1]
   return accum

#Determine if a position resides on the game board
def IsOnBoard(pos):
   if (pos >= 0) and (pos <= 63):
      return True
   else:
      return False
'''

#Determine if a piece can move to a new position
def canMove(board,pos1,pos2):
   #Assume both pieces are empty
   x = 0
   y = 0
   #Piece 1 is White
   if (board[pos1] >= 10) and (board[pos1] <= 15):
      x = 1
   #Piece 1 is Black
   if (board[pos1] >= 20) and (board[pos1] <= 25):
        x = -1
   #Piece 2 is White
   if (board[pos2] >= 10) and (board[pos2] <= 15):
        y = 1
   #Piece 2 is Black
   if (board[pos2] >= 20) and (board[pos2] <= 25):
        y = -1
   #Return product
   return x*y

#Generate possible bishop moves
def GenBishopMoves(board,pos):
   #Create list for possible moves and determine where bishop can move
   accum = []
   offsets = []

   moveRight = pos%8
   moveLeft = 7-moveRight
   moveDown = pos//8
   moveUp = 7-moveDown
            
   if min(moveRight,moveUp) >= 1:
      offsets += [[7,min(moveRight,moveUp)]]
   if min(moveRight,moveDown) >= 1:
      offsets += [[-9,min(moveRight,moveDown)]]
   if min(moveLeft,moveUp) >= 1:
      offsets += [[9,min(moveLeft,moveUp)]]
   if min(moveLeft,moveDown) >= 1:
      offsets += [[-7,min(moveLeft,moveDown)]]

   #Generate possible moves
   for i in offsets:
      for j in range(1,i[1]+1,1):
         newpos = pos+j*i[0]
         #See if bishop can move to new position
         move = canMove(board,pos,newpos)
         #Empty tile or enemy occupied
         if (move == 0) or (move == -1):
            accum += [newpos]
         #Ally or enemy occupied
         if (move == 1) or (move == -1):
            break

   #Return possible moves
   return accum

#Generate possible rook moves
def GenRookMoves(board, pos):
   #Create list for possible moves and determine where rook can move
   accum = []
   offsets = []

   moveRight = pos%8
   moveLeft = 7-moveRight
   moveDown = pos//8
   moveUp = 7-moveDown
            
   if moveRight >= 1:
      offsets += [[-1,moveRight]]
   if moveLeft >= 1:
      offsets += [[1,moveLeft]]
   if moveDown >= 1:
      offsets += [[-8,moveDown]]
   if moveUp >= 1:
      offsets += [[8,moveUp]]

   #Generate possible moves
   for i in offsets:
      for j in range(1,i[1]+1,1):
         newpos = pos+j*i[0]
         #See if rook can move to new position
         move = canMove(board,pos,newpos)
         #Empty tile or enemy occupied
         if (move == 0) or (move == -1):
            accum += [newpos]
         #Ally or enemy occupied
         if (move == 1) or (move == -1):
            break

   #Return possible moves
   return accum


#Generate possible queen moves
def GenQueenMoves(board,pos):
   #Return possible moves for rook and bishop
   return GenRookMoves(board,pos) + GenBishopMoves(board,pos)

#Generate possible king moves
def GenKingMoves(board,pos):
   #Create list for possible moves and determine where king can move
   accum = []
   offsets = []

   moveRight = pos%8
   moveLeft = 7-moveRight
   moveDown = pos//8
   moveUp = 7-moveDown
            
   if moveRight >= 1:
      offsets += [-1]
   if moveLeft >= 1:
      offsets += [1]
   if moveDown >= 1:
      offsets += [-8]
   if moveUp >= 1:
      offsets += [8]
   if min(moveRight,moveUp) >= 1:
      offsets += [7]
   if min(moveRight,moveDown) >= 1:
      offsets += [-9]
   if min(moveLeft,moveUp) >= 1:
      offsets += [9]
   if min(moveLeft,moveDown) >= 1:
      offsets += [-7]

   #Generate possible moves
   for i in offsets:
      newpos = pos+i
      #See if king can move to new position
      move = canMove(board,pos,newpos)
      #Empty tile or enemy occupied
      if (move == 0) or (move == -1):
         accum += [newpos]
  
   #Return possible moves
   return accum

def GenPawnMoves(board,pos):
   #Create list for possible moves and determine where pawn can move
   accum = []
   offsets = []
   if (pos >= 8) and (pos <= 55):
      if (board[pos] == 10):
        offsets += [8]
      elif (board[pos] == 20):
        offsets += [-8]
      if (pos % 8 < 7):
         if (board[pos] == 10):
            offsets += [9]
         elif (board[pos] == 20):
            offsets += [-7]
      if (pos % 8 > 0):
         if (board[pos] == 10):
            offsets += [7]
         elif (board[pos] == 20):
            offsets += [-9]

   #Generate possible moves
   for i in offsets:
      newpos = pos+i
      #See if pawn can move to new position
      move = canMove(board,pos,newpos) 
      #Checking in front of pawn
      if (i == 8) or (i == -8):
        #Empty tile
          if (move == 0):
             accum += [newpos]
      #Checking pawn's frontal diagonals
      else:
        #Enemy occupied
        if (move == -1):
          accum += [newpos]
  
   #Return possible moves
   return accum

def GenKnightMoves(board,pos):
   #Create list for possible moves and determine where knight can move
   accum = []
   offsets = []
   moveUp2Left1 = 1
   moveUp2Right1 = 1
   moveUp1Left2 = 1
   moveUp1Right2 = 1
   moveDown2Left1 = 1
   moveDown2Right1 = 1
   moveDown1Left2 = 1
   moveDown1Right2 = 1
   if pos == 0:
      moveUp2Left1 = 0
      moveUp2Right1 = 0
      moveUp1Left2 = 0
      moveUp1Right2 = 0
      moveDown2Left1 = 0
      moveDown1Left2 = 0
   elif pos == 1:
      moveUp2Left1 = 0
      moveUp2Right1 = 0
      moveUp1Left2 = 0
      moveUp1Right2 = 0
      moveDown1Left2 = 0
   elif pos in [2,3,4,5]:
      moveUp2Left1 = 0
      moveUp2Right1 = 0
      moveUp1Left2 = 0
      moveUp1Right2 = 0
   elif pos == 6:
      moveUp2Left1 = 0
      moveUp2Right1 = 0
      moveUp1Left2 = 0
      moveUp1Right2 = 0
      moveDown1Right2 = 0
   elif pos == 7:
      moveUp2Left1 = 0
      moveUp2Right1 = 0
      moveUp1Left2 = 0
      moveUp1Right2 = 0
      moveDown2Right1 = 0
      moveDown1Right2 = 0
   elif pos == 8:
      moveUp2Left1 = 0
      moveUp2Right1 = 0
      moveUp1Left2 = 0
      moveDown2Left1 = 0
      moveDown1Left2 = 0
   elif pos == 9:
      moveUp2Left1 = 0
      moveUp2Right1 = 0
      moveUp1Left2 = 0
      moveDown1Left2 = 0
   elif pos in [10,11,12,13]:
      moveUp2Left1 = 0
      moveUp2Right1 = 0
   elif pos == 14:
      moveUp2Left1 = 0
      moveUp2Right1 = 0
      moveUp1Right2 = 0
      moveDown1Right2 = 0
   elif pos == 15:
      moveUp2Left1 = 0
      moveUp2Right1 = 0
      moveUp1Right2 = 0
      moveDown2Right1 = 0
      moveDown1Right2 = 0
   elif pos in [16,24,32,40]:
      moveUp2Left1 = 0
      moveUp1Left2 = 0
      moveDown2Left1 = 0
      moveDown1Left2 = 0
   elif pos in [17,25,33,41]:
      moveUp1Left2 = 0
      moveDown1Left2 = 0
   elif pos in [22,30,38,46]:
      moveUp1Right2 = 0
      moveDown1Right2 = 0
   elif pos in [23,31,39,47]:
      moveUp2Right1 = 0
      moveUp1Right2 = 0
      moveDown2Right1 = 0
      moveDown1Right2 = 0
   elif pos == 48:
      moveUp2Left1 = 0
      moveUp1Left2 = 0
      moveDown1Left2 = 0
      moveDown2Left1 = 0
      moveDown2Right1 = 0
   elif pos == 49:
      moveUp1Left2 = 0
      moveDown1Left2 = 0
      moveDown2Left1 = 0
      moveDown2Right1 = 0
   elif pos in [50,51,52,53]:
      moveDown2Left1 = 0
      moveDown2Right1 = 0
   elif pos == 54:
      moveUp1Right2 = 0
      moveDown1Right2 = 0
      moveDown2Right1 = 0
      moveDown2Left1 = 0
   elif pos == 55:
      moveUp2Right1 = 0
      moveUp1Right2 = 0
      moveDown1Right2 = 0
      moveDown2Right1 = 0
      moveDown2Left1 = 0
   elif pos == 56:
      moveUp2Left1 = 0
      moveUp1Left2 = 0
      moveDown2Right1 = 0
      moveDown1Right2 = 0
      moveDown2Left1 = 0
      moveDown1Left2 = 0
   elif pos == 57:
      moveUp1Left2 = 0
      moveDown2Right1 = 0
      moveDown1Right2 = 0
      moveDown2Left1 = 0
      moveDown1Left2 = 0
   elif pos in [58,59,60,61]:
      moveDown2Right1 = 0
      moveDown1Right2 = 0
      moveDown2Left1 = 0
      moveDown1Left2 = 0
   elif pos == 62:
      moveUp1Right2 = 0
      moveDown2Right1 = 0
      moveDown1Right2 = 0
      moveDown2Left1 = 0
      moveDown1Left2 = 0
   elif pos == 63:
      moveUp2Right1 = 0
      moveUp1Right2 = 0
      moveDown2Right1 = 0
      moveDown1Right2 = 0
      moveDown2Left1 = 0
      moveDown1Left2 = 0

   if (moveUp2Right1 == 1):
      offsets += [-15]
   if (moveUp2Left1 == 1):
      offsets += [-17]
   if (moveUp1Right2 == 1):
      offsets += [-6]
   if (moveUp1Left2 == 1):
      offsets += [-10]
   if (moveDown2Right1 == 1):
      offsets += [17]
   if (moveDown2Left1 == 1):
      offsets += [15]
   if (moveDown1Right2 == 1):
      offsets += [10]
   if (moveDown1Left2 == 1):
      offsets += [6]

   #Generate possible moves
   for i in offsets:
      newpos = pos+i
      #See if knight can move to new position
      move = canMove(board,pos,newpos)
      #Empty tile or enemy occupied
      if (move == 0) or (move == -1):
        accum += [newpos]
  
   #Return possible moves
   return accum

class Tree:
   pawnEvalWhite = [ 0,  0,  0,  0,  0,  0,  0,  0,
                     50, 50, 50, 50, 50, 50, 50, 50,
                     10, 10, 20, 30, 30, 20, 10, 10,
                     5,  5, 10, 25, 25, 10,  5,  5,
                     0,  0,  0, 20, 20,  0,  0,  0,
                     5, -5,-10,  0,  0,-10, -5,  5,
                     5, 10, 10,-20,-20, 10, 10,  5,
                     0,  0,  0,  0,  0,  0,  0,  0]
   pawnEvalBlack = pawnEvalWhite[::-1]
   knightEval = [-50,-40,-30,-30,-30,-30,-40,-50,
                  -40,-20,  0,  0,  0,  0,-20,-40,
                  -30,  0, 10, 15, 15, 10,  0,-30,
                  -30,  5, 15, 20, 20, 15,  5,-30,
                  -30,  0, 15, 20, 20, 15,  0,-30,
                  -30,  5, 10, 15, 15, 10,  5,-30,
                  -40,-20,  0,  5,  5,  0,-20,-40,
                  -50,-40,-30,-30,-30,-30,-40,-50]
   bishopEvalWhite = [-20,-10,-10,-10,-10,-10,-10,-20,
                     -10,  0,  0,  0,  0,  0,  0,-10,
                     -10,  0,  5, 10, 10,  5,  0,-10,
                     -10,  5,  5, 10, 10,  5,  5,-10,
                     -10,  0, 10, 10, 10, 10,  0,-10,
                     -10, 10, 10, 10, 10, 10, 10,-10,
                     -10,  5,  0,  0,  0,  0,  5,-10,
                     -20,-10,-10,-10,-10,-10,-10,-20]
   bishopEvalBlack = bishopEvalWhite[::-1]
   rookEvalWhite = [  0,  0,  0,  0,  0,  0,  0,  0,
                       5, 10, 10, 10, 10, 10, 10,  5,
                      -5,  0,  0,  0,  0,  0,  0, -5,
                      -5,  0,  0,  0,  0,  0,  0, -5,
                      -5,  0,  0,  0,  0,  0,  0, -5,
                      -5,  0,  0,  0,  0,  0,  0, -5,
                      -5,  0,  0,  0,  0,  0,  0, -5,
                       0,  0,  0,  5,  5,  0,  0,  0]
   rookEvalBlack = rookEvalWhite[::-1]
   evalQueen = [-20,-10,-10, -5, -5,-10,-10,-20,
                  -10,  0,  0,  0,  0,  0,  0,-10,
                  -10,  0,  5,  5,  5,  5,  0,-10,
                   -5,  0,  5,  5,  5,  5,  0, -5,
                    0,  0,  5,  5,  5,  5,  0, -5,
                  -10,  5,  5,  5,  5,  5,  0,-10,
                  -10,  0,  5,  0,  0,  0,  0,-10,
                  -20,-10,-10, -5, -5,-10,-10,-20]
   kingEvalWhite = [-30,-40,-40,-50,-50,-40,-40,-30,
                     -30,-40,-40,-50,-50,-40,-40,-30,
                     -30,-40,-40,-50,-50,-40,-40,-30,
                     -30,-40,-40,-50,-50,-40,-40,-30,
                     -20,-30,-30,-40,-40,-30,-30,-20,
                     -10,-20,-20,-20,-20,-20,-20,-10,
                      20, 20,  0,  0,  0,  0, 20, 20,
                      20, 30, 10,  0,  0, 10, 30, 20]
   kingEvalBlack = kingEvalWhite[::-1]

   def __init__(self, board):
      self.board = board
      self.oldPos = 0
      self.newPos = 0
      self.score = 0
      self.children = []

   def setChildren(self,children):
      self.children = children
      return True

   def EvalBoard(self):
      counter = 0
      for i in self.board:
         if i == 10:
            self.score = self.score + 100 + Tree.pawnEvalWhite[counter]
            self.score = self.score + len(GenPawnMoves(self.board, counter))    
            offset = counter % 8
            for j in range(0,63,8):
               if (self.board[j+offset] == i) and (j+offset != counter):
                  self.score = self.score - 5
                  break
            if (counter+8 >= 0) and (counter+8 <= 63):
               if (self.board[counter+8] >= 20) and (self.board[counter+8] <= 25):
                  self.score = self.score - 5
            ally = False
            moveRight = 1
            moveLeft = 1
            moveUp = 1
            moveDown = 1
            if counter % 8 == 7:
               moveRight = 0
            if counter % 8 == 0:
               moveLeft = 0
            if int(counter / 8) == 0:
               moveUp = 0
            if int(counter / 8) == 7:
               moveDown = 0
            if moveRight ==  1:
               if (self.board[counter+1] == 10):
                  ally = True
            if moveLeft == 1:
               if (self.board[counter-1] == 10):
                  ally = True
            if moveDown == 1:
               if (self.board[counter+8] == 10):
                  ally = True
            if moveUp == 1:
               if (self.board[counter-8] == 10):
                  ally = True
            if min(moveRight,moveUp) == 1:
               if (self.board[counter-8+1] == 10):
                  ally = True
            if min(moveRight,moveDown) == 1:
               if (self.board[counter+8+1] == 10):
                  ally = True
            if min(moveLeft,moveUp) == 1:
               if (self.board[counter-8-1] == 10):
                  ally = True
            if min(moveLeft,moveDown) == 1:
               if (self.board[counter+8-1] == 10):
                  ally = True
            if (ally == False):
               self.score = self.score - 5 
         elif i == 11:
            self.score = self.score + 320 + Tree.knightEval[counter]
            self.score = self.score + len(GenKnightMoves(self.board, counter))
         elif i == 12:
            self.score = self.score + 330 + Tree.bishopEvalWhite[counter]
            self.score = self.score + len(GenBishopMoves(self.board, counter))
         elif i == 13:
            self.score = self.score + 500 + Tree.rookEvalWhite[counter]
            self.score = self.score + len(GenRookMoves(self.board, counter))
         elif i == 14:
            self.score = self.score + 900 + Tree.evalQueen[counter]
            self.score = self.score + len(GenQueenMoves(self.board, counter))
         elif i == 15:
            self.score = self.score + 20000 + Tree.kingEvalWhite[counter]
            self.score = self.score + len(GenKingMoves(self.board, counter))
         elif i == 20:
            self.score = self.score - 100 - Tree.pawnEvalBlack[counter]
            self.score = self.score - len(GenPawnMoves(self.board, counter))
            offset = counter % 8
            for j in range(0,63,8):
               if (self.board[j+offset] == i) and (j+offset != counter):
                  self.score = self.score + 5
                  break
            if (counter-8 >= 0) and (counter-8 <= 63):
               if (self.board[counter-8] >= 10) and (self.board[counter-8] <= 15):
                  self.score = self.score + 5
            ally = False
            moveRight = 1
            moveLeft = 1
            moveUp = 1
            moveDown = 1
            if counter % 8 == 7:
               moveRight = 0
            if counter % 8 == 0:
               moveLeft = 0
            if int(counter / 8) == 0:
               moveUp = 0
            if int(counter / 8) == 7:
               moveDown = 0
            if moveRight == 1:
               if (self.board[counter+1] == 20):
                  ally = True
            if moveLeft == 1:
               if (self.board[counter-1] == 20):
                  ally = True
            if moveDown == 1:
               if (self.board[counter+8] == 20):
                  ally = True
            if moveUp == 1:
               if (self.board[counter-8] == 20):
                  ally = True
            if min(moveRight,moveUp) == 1:
               if (self.board[counter-8+1] == 20):
                  ally = True
            if min(moveRight,moveDown) == 1:
               if (self.board[counter+8+1] == 20):
                  ally = True
            if min(moveLeft,moveUp) == 1:
               if (self.board[counter-8-1] == 20):
                  ally = True
            if min(moveLeft,moveDown) == 1:
               if (self.board[counter+8-1] == 20):
                  ally = True
            if (ally == False):
               self.score = self.score + 5
         elif i == 21:
            self.score = self.score - 320 - Tree.knightEval[counter]
            self.score = self.score - len(GenKnightMoves(self.board, counter))
         elif i == 22:
            self.score = self.score - 330 - Tree.bishopEvalBlack[counter]
            self.score = self.score - len(GenBishopMoves(self.board, counter))
         elif i == 23:
            self.score = self.score - 500 - Tree.rookEvalBlack[counter]
            self.score = self.score - len(GenRookMoves(self.board, counter))
         elif i == 24:
            self.score = self.score - 900 - Tree.evalQueen[counter]
            self.score = self.score - len(GenQueenMoves(self.board, counter))
         elif i == 25:
            self.score = self.score - 20000 - Tree.kingEvalBlack[counter]
            self.score = self.score - len(GenKingMoves(self.board, counter))
         counter += 1
      self.score = float(self.score)
      return self.score

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum