num1=int(input("\n\tEnter your start = "))
num2=int(input("\n\tEnter your limit = "))
for i in range(num1,num2+1):
  flag=0
  for j in range(1,i+1):
    if (i%j==0):
      flag=flag+1
  if (flag==2):
    print(i)
