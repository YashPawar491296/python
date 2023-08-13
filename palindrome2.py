a=int(input("\n Enter a string ="))
s=str(a)
l=len(s)
new =''
for i in range (0,l,1):
  new=s[i]+new
if s==new:
  print("\n\tIt is a palindrom")
else:
  print("\n\tIt is not a plaindrom")
