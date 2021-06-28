def alternatingSums(a):
 i=0
 d=1
 if d == len(a):
  a.append(0)
 while i < len(a):
  if i/2 >= 1:
   a[0]=a[0]+a[i]
   a.pop(i)
   if i < len(a):
    a[1]=a[1]+a[i]
    a.pop(i)
   i=i-1
  i=i+1
 return a 
