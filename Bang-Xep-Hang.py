n = int(input())
ds = []

for _ in range(n):
    name = input().strip()
    C, T = map(int, input().split())
    ds.append((name, C, T))

# sắp xếp
ds.sort(key=lambda x: (-x[1], x[2], x[0]))

# in kết quả
for sv in ds:
    print(sv[0], sv[1], sv[2])