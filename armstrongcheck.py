mo=int(input())
hn=mo
sum=0
while mo>0:
    rem=mo%10
    sum=sum+(rem**3)
    mo=mo//10
if sum==hn:
    print("yes")
else:
    print("no")
