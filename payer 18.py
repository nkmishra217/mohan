m=int(input())
cocount=0
count=1
n=input()
for i in range(1,m):
    k=input()
    if len(k)==len(n):
        for j in k:
            if j in n:
              cocount+=1
            if len(n)==cocount:
                count=count+1
                
    
    
print(count)
