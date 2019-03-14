from queue import *
from binary_tree import *

class tree:
   def __init__(self,x):
      self.store = [x,[]]

   def AddSuccessor(self,x):
      self.store[1] = self.store[1] + [x]
      return True

   def Print_DepthFirst(self):
      self.Print_DepthFirst_helper("")
      return True
   
   def Print_DepthFirst_helper(self, indent):
      print(indent+str(self.store[0]))
      for i in self.store[1]:
         i.Print_DepthFirst_helper(indent+"   ")
      return True


   def Get_LevelOrder(self):
      x = queue()
      x.enqueue(self.store)
      accum = []
      while (x.cnt != 0):
         r = x.dequeue()
         accum += [r[1][0]]
         for i in r[1][1]:
            x.enqueue(i.store)
      return accum

   def ConvertToBinaryTree(self):
      return self.ConvertToBinaryTree_helper([])

   def ConvertToBinaryTree_helper(self, siblings):
      left_node = False
      right_node = False
      if len(self.store[1]) == 1:
         left_node = self.store[1][0].ConvertToBinaryTree_helper([])
      elif len(self.store[1]) > 1:
         left_node = self.store[1][0].ConvertToBinaryTree_helper(self.store[1][1:])
      if len(siblings) == 1:
         right_node = siblings[0].ConvertToBinaryTree_helper([])
      elif len(siblings) > 1:
         right_node = siblings[0].ConvertToBinaryTree_helper(siblings[1:])
      node = binary_tree(self.store[0])
      if left_node != False:
         node.AddLeft(left_node)
      if right_node != False:
         node.AddRight(right_node)
      return node

class binary_tree:
   def __init__(self, val):
      self.store = [val, False, False]

   def AddLeft(self, subtree):
      if self.store[1] != False:
         return False
      else:
         self.store[1] = subtree
         return True

   def AddRight(self, subtree):
      if self.store[2] != False:
         return False
      else:
         self.store[2] = subtree
         return True

   def Print_DepthFirst(self):
      self.Print_DepthFirst_helper("")
      return True

   def Print_DepthFirst_helper(self, indent):
      print(indent+str(self.store[0]))
      for i in self.store[1:]:
         if type(i) == binary_tree:
            i.Print_DepthFirst_helper(indent+"   ")
      return True

   def Get_LevelOrder(self):
      x = queue()
      x.enqueue(self.store)
      accum = []
      while (x.cnt != 0):
         r = x.dequeue()
         accum += [r[1][0]]
         if type(r[1][1]) == binary_tree:
            x.enqueue(r[1][1].store)
         if type(r[1][2]) == binary_tree:
            x.enqueue(r[1][2].store) 
      return accum

   def ConvertToTree(self):
      if self.store[2] != (not True):
         return [(not True)]
      cTree = tree(self.store[0])
      if self.store[1] != (not True):
         cTree.store[1] = self.ConvertToTree_helper()
      return [True, cTree]

   def ConvertToTree_helper(self):
      siblings = []
      if self.store[1] == (not True):
         return tree(self.store[0])
      left_node = self.store[1]
      while True:
         if left_node == (not True):
            break
         next_node = tree(left_node.store[0])
         if left_node.store[1] != (not True):
            next_node.store[1] = left_node.ConvertToTree_helper()
         siblings = siblings + [next_node]
         left_node = left_node.store[2]
      return siblings

class queue:
    def __init__(self):
        self.store=[]
        self.cnt = 0

    def enqueue(self,value):
        self.store=self.store+[value]
        self.cnt = self.cnt + 1
        return self.cnt

    def dequeue(self):
        if (self.cnt==0):
            return [False,0]
        else:
            r=self.store[0]
            self.cnt=self.cnt-1
            self.store=self.store[1:]
            return [True,r]
