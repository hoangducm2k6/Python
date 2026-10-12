n=int(input())
a=[]
for i in range(n):
    s=input()
    a.append(s)
    a=sorted(set(a))
print(len(a))