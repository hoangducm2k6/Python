n = int(input())

subjects = []

for _ in range(n):
    code = input().strip()
    name = input().strip()
    form = input().strip()

    subjects.append((code, name, form))


subjects.sort(key=lambda x: x[0])


for s in subjects:
    print(s[0], s[1], s[2])