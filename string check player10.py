    
mo,h=list(map(str,input().split()))
count=0
for i in range(0,len(mo)):
    if(mo[i]!=h[i]):
        count+=1
if(count==1):
    print("yes")
else:
    print("no")
