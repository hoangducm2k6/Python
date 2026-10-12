t=int(input())
for _ in range(t):
    s=input()
    tong=int(s[0])
    ok=True
    for i in range(1,len(s)):
        tong+=int(s[i])
        if abs(int(s[i])-int(s[i-1])) != 2:
            ok=False
    if tong%10!=0:
        ok=False
    if ok:
        print("YES",end="\n")
    else:
        print("NO",end="\n")