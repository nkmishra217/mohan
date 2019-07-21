m=input()
count=0
for i in m:
  if m.count(i)>count:
    mo=i
    count=m.count(i)
print(mo)
