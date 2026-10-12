t=int(input())
for  _ in range(t):
    s=input()
    ok=True
    tong=0
    for i in range(len(s)):
        tong+=int(s[i])
        if int(s[i])%2==0 and i %2==1:
            ok=False

        if int(s[i])%2==1 and i %2==0:
            ok=False

    if tong<2:
        ok=False
    for i in range(2,int(tong**0.5)+1):
        if tong%i==0:
            ok=False
    if ok:
        print("YES")
    else:
        print("NO")