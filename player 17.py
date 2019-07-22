n,m=map(int,input().split())
if n>m:
    maxi=n
else:
    maxi=m
while(True):
    if (maxi%n==0)and(maxi%m==0):
        low=maxi
        break
    maxi=maxi+1
print(low)
        
