moh=int(input())
mo=list(map(int,input().split()))
if len(mo)==moh:
    mo.sort(reverse=True)
    m=[str(i) for i in mo]
    n=int("".join(m))
    print(n)
