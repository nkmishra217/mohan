n,m=map(int,input().split())
if n>m:
    maxi=n
else:
    maxi=m
i=1
while(True):
    if (maxi%n==0)and(maxi%m==0):
        low=maxi
        break
    i=i+1
    maxi=maxi*i
print(low)
        
