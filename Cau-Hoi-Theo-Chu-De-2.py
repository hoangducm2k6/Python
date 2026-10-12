n=int(input())
a=[input() for _ in range(n)]
d=""
dem=0
for i in range(n):
    if a[i]=="":
        if d!="":
            print(d+": "+ str(dem))
        d=""
        dem=0
    else:
        if d=="":
            d=a[i]
        else:
            dem+=1
if d!="":
    print(d+": "+ str(dem))