n = int(input())
a = list(map(int, input().split()))

mx = max(a)

max_len = 0
cur = 0

for x in a:
    if x == mx:
        cur += 1
        max_len = max(max_len, cur)
    else:
        cur = 0

print(max_len)