s1=input("\nEnter a string = ")
s2=input("\nEnter a string = ")
s3=len(s1)
s4=len(s2)
c1=0
for i in s1 :
  if i in s2 :
    c1=c1+1
c2=0
for i in s2 :
  if i in s1 :
      c2=c2+1
if (c1==c2) and (s3==s4) :
      print("\nthis is a anagram\n")
else :
    print("\nThis is not a anagram")
