a=int(input("\nEnter your limit ="))
f1=0
f2=1
print("\n Your series is =\n")
print(f1)
print(f2)
for i in range(1,a-1,1):
   next=f1+f2
   f1=f2
   f2=next
   print(next)
