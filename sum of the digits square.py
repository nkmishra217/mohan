mo=int(input())
l=0
while mo>0:
    m=mo%10
    l=l+m**2
    mo=mo//10
    
print(l)
