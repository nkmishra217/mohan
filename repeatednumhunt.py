mo=int(input())
mohan=list(map(int,input().split()))
ln=[]
for i in mohan:
    if mohan.count(i)>1:
        if str(i) not in ln:
            ln.append(str(i))
if len(ln)==0:
    print("unique")
else:
    print(" ".join(ln))
