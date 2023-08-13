a=int(input("\nEnter a number ="))
s=str(a)
l=len(s)
c=0
for i in range (0,l,1):
    b=(int(s[i]))**l
    c=c+b
if c==a :
  print("\nThis number is a Armstrong")
else :
  print("\nThis number is not a Armstrong")
