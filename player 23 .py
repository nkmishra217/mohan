n,m=map(int,input().split())
s=input()
l=list(map(int,input().split()[:n]))
a=list(map(int,input().split()[:m]))
for i in a:
  l.append(i)
  print(max(l),end=" ")
