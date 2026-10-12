t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    i=j=l=0
    res=[]
    while i<n and j<m and l<k:
        if a[i]==b[j]==c[l]:
            res.append(a[i])
            i+=1
            j+=1
            l+=1
        else:
            mm=min(a[i],b[j],c[l])
            if a[i]==mm:
                i+=1
            elif b[j]==mm:
                j+=1
            else:
                l+=1
    if res:
        print(*res)
    else:
        print("NO")
