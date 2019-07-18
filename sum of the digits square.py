mo=int(input())
l=0
while mo>0:
    mo=mo%10
    l=l+mo**2
    mo=mo//10
    
print(l)
