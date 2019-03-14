from chessPlayer_tree import *
from chessPlayer_queue import *

def IsPositionUnderThreat(board,position,player):
   enemy = 10
   if player == 10:
      enemy = 20
   pieces = GetPlayerPositions(board,enemy)
   for i in pieces:
      moves = GetPieceLegalMoves(board,i)
      for move in moves:
         if move == position:
            return True
   return False

def GenCandidateMoves (node, depth, alpha, beta, player):
   if depth == 0:
      #print(node.EvalBoard())
      return [node.EvalBoard(), []]
   rnode = node
   rscore = 0
   GenCandidateMoves_nextMoves(player,node)
   if player == 10:
      rscore = -float("inf")
      for child in node.children:
         oldscore = rscore
         rscore = max(rscore, GenCandidateMoves(child, depth-1, alpha, beta, 20)[0])
         if oldscore != rscore:
            rnode = child
         alpha = max(alpha, rscore)
         if alpha >= beta:
            break
   else:
      rscore = float("inf")
      for child in node.children:
         oldscore = rscore
         rscore = min(rscore, GenCandidateMoves(child, depth-1, alpha, beta, 10)[0])
         if oldscore != rscore:
            rnode = child
         beta = min(beta, rscore)
         if alpha >= beta:
            break
   #print("\t"*depth + "%s" % rscore)
   rnode.score = rscore
   node.score = rscore
   return [rscore, rnode]

def GenCandidateMoves_nextMoves(player,tree):
   accum = []
   pieces = GetPlayerPositions(tree.board, player)
   for i in pieces:
      moves = GetPieceLegalMoves(tree.board, i)
      #print(moves)
      for move in moves:
            tmp = tree.board[move]
            tree.board[move] = tree.board[i]
            tree.board[i] = 0
            #print(printBoard(tree.board))
            '''
            kingPos = index_of(player+5,tree.board)
            if (kingPos != -1):
              if(IsPositionUnderThreat(tree.board,kingPos,player) == False):
            '''
            child = Tree(tree.board[:])
            child.oldPos = i
            child.newPos = move
            accum += [child]
            tree.board[i] = tree.board[move]
            tree.board[move] = tmp
   tree.setChildren(accum)
   return True

def index_of(val, in_list):
    try:
        return in_list.index(val)
    except ValueError:
        return -1

def chessPlayer(board,player):
   if board == []:
      return [False,-1,-1,-1]
   if not(player == 10 or player == 20):
      return [False,-1,-1,-1]
   tree = Tree(board)
   best = GenCandidateMoves(tree, 3, -float("inf"), float("inf"), player)
   candidateMoves = []
   for i in tree.children:
      #print("FINAL: %s" % i.score)
      candidateMoves = candidateMoves + [[[i.oldPos,i.newPos],i.score]]
   evalTree = Get_LevelOrder(tree)
   return [True,[best[1].oldPos,best[1].newPos],candidateMoves,evalTree]

def Get_LevelOrder(tree):
        x=queue()
        x.enqueue(tree)
        accum=[]
        while True:
            y=x.dequeue()
            # y is a 2-list where y[0]=True/False
            # and y[1] is the actual dequeued value when y[0]=True
            if (y[0]==False):
                break
            else:
                v=y[1]
                accum=accum+[v]
                for i in v.children:
                    x.enqueue(i)
        return accum