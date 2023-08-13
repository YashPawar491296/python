year=int(input("\n\tEnter any year = "))
if year%4==0:
  ans="\nThis is a leap year"
else:
  ans="\nTis is not a leap year"
if year%100==0:
  if year%400==0:
    ans="\nThis is a leap year"
  else:
    ans="\nThis is not a leap year"
print(ans)
