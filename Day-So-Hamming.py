import bisect

MAXN = 10 ** 18
hamming = []

a = 1
while a <= MAXN:
    b = a
    while b <= MAXN:
        c = b
        while c <= MAXN:
            hamming.append(c)
            c *= 5
        b *= 3
    a *= 2

hamming = sorted(set(hamming))

t = int(input())
for _ in range(t):
    n = int(input())

    pos = bisect.bisect_left(hamming, n)

    if pos < len(hamming) and hamming[pos] == n:
        print(pos + 1)
    else:
        print("Not in sequence")

