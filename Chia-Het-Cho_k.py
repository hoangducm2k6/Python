a, k, n = map(int, input().split())

b=a//k +1
c=n//k
d=0
for i in range(b,c+1):
    print(k*i-a,end=" ")
    d+=1
if (d==0):
    print(-1)
