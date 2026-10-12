t=int(input())
a=[]
for _ in range(t):
    s=input().strip()
    a.append(s)
    a=sorted(set(a))
print(len(a))