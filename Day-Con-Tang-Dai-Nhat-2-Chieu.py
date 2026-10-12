from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

# QUAN TRỌNG
a.sort(key=lambda x: (x[0], -x[1]))

lis = []

for _, y in a:
    pos = bisect_left(lis, y)
    if pos == len(lis):
        lis.append(y)
    else:
        lis[pos] = y

print(len(lis))