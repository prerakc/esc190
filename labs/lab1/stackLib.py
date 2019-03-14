class Stack:
   def __init__ (self):
      self.data = []
   
   def push (self, value):
      self.data = self.data + [value]
      return True

   def pop (self):
      self.value = self.data[len(self.data)-1]
      self.data = self.data[:len(self.data)-1]
      return self.value
   
