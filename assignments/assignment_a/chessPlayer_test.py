from chessPlayer import *
from time import *
from random import *

def getPiece(name):
   if name=="pawn":
      return 0
   elif name=="knight":
      return 1
   elif name=="bishop":
      return 2
   elif name=="rook":
      return 3
   elif name=="queen":
      return 4
   elif name=="king":
      return 5
   else:
      return -1

def genBoard():
   r=[0]*64
   White=10
   Black=20
   for i in [ White, Black ]:
      if i==White:
         factor=+1
         shift=0
      else:
         factor=-1
         shift=63

      r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
      r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
      r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
      if i==White:
         r[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*3] = i+getPiece("king")
      else:
         r[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*4] = i+getPiece("king")

      for j in range(0,8):
         r[shift+factor*(j+8)] = i+getPiece("pawn")

   return r

board = genBoard()

'''
board = [13,11,12,15,14,12,11,13,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
23,21,22,25,24,22,21,23]
'''

def playerW(board):
   tree = Tree(board)
   start = time.time()
   best = GenCandidateMoves(tree, 4, -float("inf"), float("inf"), 10)

   end = time.time()
   print("TIME IS " + str(end-start))

   return [best[1].oldPos,best[1].newPos]

def playerB_random(board):
   accum = []
   for i in GetPlayerPositions(board,20):
      for j in GetPieceLegalMoves(board,i):
            tmp = list(board)
            tmp[j] = tmp[i]
            tmp[i] = 0
            if (IsPositionUnderThreat(tmp,index_of(25,tmp),20) == False):
               accum += [[i,j]]

   if (accum != []):
      pair = accum[randint(0,len(accum)-1)]
      piece = pair[0]
      move = pair[1]
      print("BLACK IS RANDOMLY MOVING PIECE %s FROM INDEX %s TO INDEX %s." % (board[piece],piece,move))
      return [True,[piece,move],[],[]]
   else:
      return False

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum

def gamePlaying(board):
   WKingAlive = False
   BKingAlive = False
   for i in board:
      if i == 15:
         WKingAlive = True
      elif i == 25:
         BKingAlive = True
   if (WKingAlive == True) and (BKingAlive == True):
      return True
   else:
      False

counter = 0
move = 0
length = 0
while (gamePlaying(board)):
   if counter % 2 == 0:
      start = process_time()
      move = chessPlayer(board,10)
      end = process_time()
      length = end-start
   else:
      start = process_time()
      move = playerB_random(board)
      #move = chessPlayer(board,20)
      end = process_time()
      length = end-start
      if move == False:
         break
      #move = playerB(board)

   if counter % 2 == 0:
      print("WHITE IS MOVING PIECE %s FROM INDEX %s TO INDEX %s." % (board[move[1][0]],move[1][0],move[1][1]))
   board[move[1][1]] = board[move[1][0]]
   board[move[1][0]] = 0
   print(printBoard(board))
   print()
   sleep(5)
   print(move[3])
   print()
   print(move[2])
   print(move[0])
   print(move[1])
   print("TIME: %s" % length)
   print()
   sleep(5)
   counter += 1
print("GAME OVER")