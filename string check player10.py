    
m,h=map(str,input().split())
if(len(m)!=len(h)):
    print("no")
else :
    s1=[m.count(i) for i in m]
    s2=[h.count(i) for i in h]
if(s1==s2):
    print("yes")
else:
    print("no")
