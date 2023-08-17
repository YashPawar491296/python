n=int(input("\n Enter the size = "))
name=[]
number=[]
for i in range(n):
  nm=input("\n\nEnter name= ")
  name.append(nm)
  num=int(input("Entet the number = "))
  number.append(num)
flag=0
search=input("\n\tEnter the name = ")
for i in range(n):
  if search==name[i]:
    print("\n\tContact number = ",number[i])
    flag=1
if flag==0:
  print("\n\tContact not found")
