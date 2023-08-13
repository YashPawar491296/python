a=int(input("\nEnter a number = "))
s=str(a)
l=len(s)
flag=0
for i in range (0,l,1):
  c=int(s[i])
  flag=flag+1
if c==0 or c==1:
  if flag==l:
     print("\n\tThis is a binary number")
else :
  print("\n\tThis is not a binary number")
