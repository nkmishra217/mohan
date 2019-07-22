m=int(input())

for i in range(2,m+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if m%i==0:
            print(i,end=" ")
        
