
a=list(map(int,input().split()))
while a!=[0,0,0,0]:
    d=0
    while not (a[0]==a[1]==a[2]==a[3]):
        b=[0]*4
        b[0]=abs(a[0]-a[1])
        b[1]=abs(a[1]-a[2])
        b[2]=abs(a[2]-a[3])
        b[3]=abs(a[3]-a[0])
        a=b
        d+=1
    print(d)
    a=list(map(int,input().split()))