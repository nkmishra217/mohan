moh=int(input())
mo=list(map(int,input().split()))
count=dict()
for word in mo:
    if word not in count:
        count[word]=1
    else:
        count[word]+=1
for word in mo:
    if (count[word]==1):
        print(word)
