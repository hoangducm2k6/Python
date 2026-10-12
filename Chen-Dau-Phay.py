s=input().strip()
rev=s[::-1]
res=[]
for i in range(0,len(rev),3):
    res.append(rev[i:i+3])
print(",".join(res)[::-1])