t=int(input())
for _ in range(t):
    n=input()
    d=0

    ok=True
    for i in range(len(n)):
        d += int(n[i])
    for i in range(len(n)-1):

       if abs(int(n[i])-int(n[i+1])) !=2:
           ok=False
    if d%10!=0:
        ok=False

    if ok:
        print("YES")
    else:
        print("NO")