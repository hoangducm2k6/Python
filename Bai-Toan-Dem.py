n = int(input())
a = []


while len(a) < n:
    a += list(map(int, input().split()))

a_set = set(a)

missing = []
for i in range(1, max(a) + 1):
    if i not in a_set:
        missing.append(i)

if not missing:
    print("Excellent!")
else:
    for x in missing:
        print(x)





