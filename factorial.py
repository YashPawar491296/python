num=int(input("\n\tEnter a number = "))
# num2=num-1
add=0
fact=1
for i in range(num-1,0,-1):
   fact=num*i
   num=fact
print("Factorial of given number is = ",fact)
