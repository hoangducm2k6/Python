import bisect
hamming=[]
MAX=10**18
a=1
while a<=MAX:
    b=a
    while b<=MAX:
        c=b
        while c<=MAX:
            hamming.append(c)
            c*=5
        b*=3
    a*=2
hamming=sorted(set(hamming))
t=int(input())
for _ in range(t):
    n=int(input())
    res=bisect.bisect_left(hamming,n)
    if res<len(hamming) and hamming[res]==n:
        print(res+1)
    else:
        print("Not in sepuence")

