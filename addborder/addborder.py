def addBorder(picture):
 i=1
 d=len(picture)
 s=len(picture[0])
 picture.insert(0,"*"*(s+2))
 picture.append("*"*(s+2))
 while i<d+1:
  picture[i]="*"+picture[i]+"*"
  i=i+1
 return picture
