from queue import *

class tree:
    def __init__(self,x):
        self.store = [x,[]]

    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True

    def GetSuccessors(self):
        return self.store[1]

    def Print_DepthFirst(self):
        self.Print_DepthFirst_helper("   ")
        return True


    def Print_DepthFirst_helper(self,prefix):
        print prefix+str(self.store[0])
        for i in self.store[1]:
            i.Print_DepthFirst_helper(prefix+"   ")
        return True

    def Get_LevelOrder(self):
        x=queue()
        x.enqueue(self.store)
        accum=[]
        while True:
            y=x.dequeue()
            # y is a 2-list where y[0]=True/False
            # and y[1] is the actual dequeued value when y[0]=True
            if (y[0]==False):
                break
            else:
                v=y[1]
                accum=accum+[v[0]]
                for i in v[1]:
                    x.enqueue(i.store)
        return accum

#Given a node N in a general tree:
#Let [L, REST_SUCC] be the successors of N
#Let S=[R, REST_SIB] be the siblings of N
# (Note: REST_X is a list of Trees)
#Then:
#def f(N,S):
#   T=tree(N)
#   T.L = f(L,REST_SUCC)
#   T.R = f(R,REST_SIB)
#   return T

    def Gen_BinaryTree_helper(self,Siblings):
        Root = self.store[0]
        # Left ST
        x=self.GetSuccessors()
        if len(x) == 0:
            Left = []
        else:
            if len(x) < 2:
                LeftSiblings=[]
            else:
                LeftSiblings=self.GetSuccessors()[1:]
            Left = self.GetSuccessors()[0].Gen_BinaryTree_helper(LeftSiblings)
        if Siblings == []:
            Right = []
        else:
            if len(Siblings) < 2:
                RightSiblings=[]
            else:
                RightSiblings=Siblings[1:]
            Right = Siblings[0].Gen_BinaryTree_helper(RightSiblings)
        rval=tree(Root)
        if Left <> []:
            rval.AddSuccessor(Left)
        if Right <> []:
            rval.AddSuccessor(Right)
        return rval

    # calling this function on a node will return a
    # tree consisting of the node and its successors
    def GBinaryTreeToGenTree_helper(self):
      Root = self.store[0]
      rval = tree(Root)
      x=self.GetSuccessors()
      #print "DEBUG: ",Root,"x",x
      if len(x) != 0:
          s = x[0] # L
          #print "DEBUG: Root",Root,"s (Left)",s.store
          while True:
             m = s.GBinaryTreeToGenTree_helper()
             rval.AddSuccessor(m)
             #print "Add Succ: Root=",Root,"succ=",m.store[0]
             ss = s.GetSuccessors()
             if len(ss) == 2:
                s = ss[1]
             else:
                break
      return rval
