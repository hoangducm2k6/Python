from itertools import product
n=int(input())
d=['2','3','5','7']
for i in range(4,n+1):
    for p in product(d,repeat=i):
        s=''.join(p)
        if s[-1]!='2':
            if all(c in s for c in d):
                print(s)