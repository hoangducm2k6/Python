n,k=map(int,input().split())
s=input().split()
s=sorted(set(s))
a=[]
def backtrack(strat):
    if len(a)==k:
        print(*a)
        return
    for i in range(strat,len(s)):
        a.append(s[i])
        backtrack(i+1)
        a.pop()
backtrack(0)