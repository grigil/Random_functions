def sortByHeight(a):
 b=0
 k=0
 while k < len(a):
  i=0
  while i < len(a):
   if a[i]!=-1:
    if a[k]!=-1:
     if a[k]<a[i]:
      b=a[i]
      a[i]=a[k]
      a[k]=b
   i=i+1
  k=k+1
 return a

    a
