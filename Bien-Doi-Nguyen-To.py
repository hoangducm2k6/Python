MAX = 10000


b = [True] * (MAX + 1)
b[0] = b[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if b[i]:
        for j in range(i*i, MAX+1, i):
            b[j] = False


res = [i for i in range(MAX+1) if b[i]]


m = int(input())
a = list(map(int, input().split()))

dem = 0

for i in a:
    if not b[i]:
        gan_nhat = min(res, key=lambda j: abs(j - i))
        dem =max(abs(gan_nhat - i),dem)

print(dem)