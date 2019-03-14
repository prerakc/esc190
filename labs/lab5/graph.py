class stack:
    def __init__(self):
        self.store=[]
        self.cnt = 0

    def add(self,value):
        self.store=self.store+[value]
        self.cnt = self.cnt + 1
        return self.cnt

    def remove(self):
        if (self.cnt==0):
            return [False,0]
        else:
            r=self.store[len(self.store)-1]
            self.cnt=self.cnt-1
            self.store=self.store[0:len(self.store)-1]
            return [True,r]

class queue:
    def __init__(self):
        self.store=[]
        self.cnt = 0

    def add(self,value):
        self.store=self.store+[value]
        self.cnt = self.cnt + 1
        return self.cnt

    def remove(self):
        if (self.cnt==0):
            return [False,0]
        else:
            r=self.store[0]
            self.cnt=self.cnt-1
            self.store=self.store[1:]
            return [True,r]

class graph:
   def __init__(self):
      self.v = []
      self.e = []
      self.w = []
      self.counter = 0

   def addVertex(self,n):
      for i in range(0,n,1):
         self.v += [self.counter]
         self.counter += 1
      return len(self.v)

   def addEdge(self,from_idx,to_idx,directed,weight):
      if (weight == 0):
         return False
      if (from_idx < 0) or (to_idx >= self.counter):
         return False
      self.e += [[from_idx,to_idx]]
      self.w += [weight]
      if (directed == False):
         self.e += [[to_idx,from_idx]]
         self.w += [weight]
      return True

   def traverse(self,start,typeBreath):
      if type(start) == int:
         if (start < 0) or (start >= self.counter):
            return []
      else:
         if (start != None):
            return []
      if type(typeBreath) != bool:
         return []
      c = None
      if typeBreath == True:
         c = queue()
      if typeBreath == False:
         c = stack()
      discovered = [False]*self.counter
      processed = [False]*self.counter
      verticies = []
      if start == None:
         verticies = self.v
      else:
         verticies = [start]
      accum = []
      for item in verticies:
         saccum = []
         if discovered[item] == False:
            c.add(item)
            discovered[item] = True
         while (c.cnt != 0):
            status,m = c.remove()
            if (processed[m] == False):
               saccum = saccum + [m]
               processed[m] = True
            tmp = []
            for i in self.e:
               if i[0] == m:
                  tmp += [i[1]]
            #tmp.sort()
            for x in tmp:
               if discovered[x] == False:
                  c.add(x)
                  discovered[x] = True
         if saccum != []:
            accum += [saccum]
      if start == None:
         return accum
      else:
         return accum[0]

   def connectivity(self,vx,vy):
      forward = self.traverse(vx,False)
      backward = self.traverse(vy,False)
      return [vy in forward,vx in backward]

   def path(self,vx,vy):
      forward = self.traverse(vx,False)
      backward = self.traverse(vy,False)
      o1 = []
      o2 = []
      if vy in forward:
         o1 = [vy]
         tmp = vy
         while tmp != vx:
            for i in [x for x in self.e if x[1] == tmp]:
               if (i[0] in forward):
                  o1 += [i[0]]
                  tmp = i[0]
                  break
         o1.reverse()
      if vx in backward:
         o2 = [vx]
         tmp = vx
         while tmp != vy:
            for i in [x for x in self.e if x[0] == tmp]:
               if (i[1] in backward):
                  o2 += [i[1]]
                  tmp = i[1]
                  break
         o2.reverse()
      return [o1,o2]
