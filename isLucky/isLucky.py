def isLucky(n):
 x=0
 y=0
 d=str(n)
 for i in range(len(d)):
  if i > ((len(d)-1)//2):
   x=int(d[i])+x
  elif i <= ((len(d)-1)//2):
   y=y+int(d[i])
 if x == y:
  return True
 else:
  return False
