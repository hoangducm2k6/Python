n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[0]*(m+1)
b.append(0)
for i in a:
    b[i]+=1
max1=max(b)
max2=0

for i in b:
    if i!= max1 and max2<i:
        max2=i

if max2==0:
    print("NONE")
else:
    print(b.index(max2))