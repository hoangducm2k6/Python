n = int(input())
a = list(map(int, input().split()))

res = float('inf')

for k in range(0, max(a) + 1):
    total = 0
    ok = True

    for x in a:
        if k == 0:
            b = x + 1
        else:
            b = x // (k + 1) + 1

        if x // b != k:
            ok = False
            break

        total += b

    if ok:
        res = min(res, total)

print(res)