s=input()
s=s[::-1]
res=[]
for i in range(0,len(s),3):
    res.append(s[i:i+3])
print(",".join(res)[::-1])