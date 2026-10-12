s = input().strip()
lower=0
upper=0
for ch in s:
    if ch.islower():
        lower+=1
    else:
        upper+=1
if (lower>=upper):
    print(s.lower())
else:
    print(s.upper())