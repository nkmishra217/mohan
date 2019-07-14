mo=int(input())
for i in range(2,mo):
    if mo%i==0:
        print("no")
        break
else:
    print("yes")
