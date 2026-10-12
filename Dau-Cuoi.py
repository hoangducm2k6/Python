t=int(input())
for _ in range(t):
    s=input().strip()
    if s[:2]==s[-2:]:
        print("YES")
    else:
        print("NO")