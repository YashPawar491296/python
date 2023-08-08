print("Your choices are :- \n\t a=add \n\t b=sub \n\t c=mul \n\t d=div \n\t e=rem \n\t f=pow \n\t g=fdiv\n\n")
option=input("enter your option = ")

if option=='a':

   a=int(input("Enter A = "))
   b=int(input("Enter B = "))
   print("Addition of A and b = ",a+b)
 elif option=='b':
   a=int(input("Enter A = "))
   b=int(input("Enter B = "))
   print("Subtraction of A and b = ",a-b)
 elif option=='c':
   a=int(input("Enter A = "))
   b=int(input("Enter B = "))
   print(" Multiplication of A and b = ",a*b)
 elif option=='d':
   a=int(input("Enter A = "))
   b=int(input("Enter B = "))
   print("division of A and b = ",a/b)  
 elif option=='e':
   a=int(input("Enter A = "))
   b=int(input("Enter B = "))
   print("Remaining of A and b = ",a%b)
 elif option=='f':
   a=int(input("Enter A = "))
   b=int(input("Enter B = "))
   print("Power of A and b = ",a**b)
 else:
   a=int(input("Enter A = "))
   b=int(input("Enter B = "))
   print("Floor division of A and b = ",a//b)
