n,m=map(int,input().split())
if (n<m):
  mini=n
else:
  mini=m
l=[]
for i in range(1,mini+1):
  if (n%i==0) and (m%i==0):
    l.append(i)
print(max(l))
  
