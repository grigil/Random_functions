def phoneCall(min1, min2_10, min11, s):
  d=0
  while s>0:
    s=s-min1
    if s<0:
      break
    d=d+1
    if d>0:
      break
  while s>0:
    s=s-min2_10
    if s<0:
      break
    d=d+1
    if d>9:
      break
  while s>0:
    s=s-min11
    if s<0:
      break
    d=d+1
  return d
