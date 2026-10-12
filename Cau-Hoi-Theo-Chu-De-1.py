n = int(input())
a = [input() for _ in range(n)]

topic = ""
count = 0

for i in range(n):
    if a[i] == "":
        if topic != "":
            print(topic + ": " + str(count))
        topic = ""
        count = 0
    else:
        if topic == "":
            topic = a[i]
        else:
            count += 1


if topic != "":
    print(topic + ": " + str(count))