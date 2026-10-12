t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a=sorted(a)
    b=sorted(b)
    d=0
    for i in range(n):
        if a[i]>b[i]:
            d+=1
    if d==0:
        print("YES",end="\n")
    else:
        print("NO",end="\n")