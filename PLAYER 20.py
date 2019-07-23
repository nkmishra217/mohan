m=input()
s=" "
for i in m:
  if (i>="A") and (i<="V"):
    h=chr(ord(i)+3)
    s=s+h
  else:
    h=chr(ord(i)-23)
    s=s+h
print(s)
