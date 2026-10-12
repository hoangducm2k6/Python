def nt(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
t=int(input())
for _ in range(t):
    s=input().strip()
    dem=0
    for ch in s:
        d=int(ch)
        if nt(d):
            dem+=1
    if dem*2>(len(s)) and nt(len(s)):
        print("YES")
    else:
        print("NO")