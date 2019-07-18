def shift(l, n):
   return l[n+1:] + l[:n+1]
m,n=map(int,input().split())
l=list(map(int,input().split()))
u=(shift(l,n))
print(*u)
