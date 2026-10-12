def nt(a):
    if a<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
t=int(input())
for _ in range(t):
    s=input()
    d=int(s[:3])
    c=int(s[-3:])
    if nt(d) and nt(c):
        print("YES")
    else:
        print("NO")
