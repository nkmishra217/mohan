mo,mo1=map(int,input().split())
for mo2 in range(mo+1,mo1):
    temp=mo2
    sum=0
    while mo2>0:
      rem=mo2%10
      sum=sum+(rem**3)
      mo2=mo2//10
    if sum==temp:
       print(sum)
    else:
       pass
