a=input("\n Enter a string =")
l=len(a)
new =''
for i in range (0,l,1):
  new=a[i]+new
if a==new:
  print("\n\tIt is a palindrom")
else:
  print("\n\tIt is not a plaindrom")
