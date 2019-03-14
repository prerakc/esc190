from stackLib import *

def bc (string):
   s = Stack()
   passed = True;
   n = 0
   elem = 0

   for i in range(0,len(string),1):
      elem = elem + 1
      value = string[i]

      if ((value == '{') or (value == '[') or (value == '(')):
         s.push(value)
         n = n + 1

      if ((value == '}') or (value == ']') or (value == ')')):
         if (n == 0):
            passed = False
            break

         popped = s.pop()
         n = n - 1

         if ((popped == '{') and (value == '}')):
            continue
         elif ((popped == '[') and (value == ']')):
            continue
         elif ((popped == '(') and (value == ')')):
            continue
         else:
            passed = False
            break

   if ((n != 0) or (passed == 0)):
      return [False,elem]
   else:
      return [True,-1]

def main ():
   print(bc("(()()()())")[0],bc("(()()()())")[1],"\n")
   print(bc("(((())))")[0],bc("(((())))")[1],"\n")
   print(bc("(()((())()))")[0],bc("(()((())()))")[1],"\n")
   print(bc("((((((())")[0],bc("((((((())")[1],"\n")
   print(bc("()))")[0],bc("()))")[1],"\n")
   print(bc("(()()(()")[0],bc("(()()(()")[1],"\n")

main()
