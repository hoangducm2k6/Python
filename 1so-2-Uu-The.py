from collections import deque

def check(s):
    return s.count('2')>len(s)//2
t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    d=deque(['1','2'])
    while len(a)<n:
        s=d.popleft()
        if check(s):
            a.append(s)
        d.append(s+'0')
        d.append(s+'1')
        d.append(s+'2')
    print(*a)