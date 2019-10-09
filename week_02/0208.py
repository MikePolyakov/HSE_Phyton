# while
now = int(input())
maxN = now
while now != 0:
    now = int(input())
    if now == 0:
        break
    if now > maxN:
        maxN = now
print(maxN)1


now = int(input())
maxN = now
while now != 0:
    now = int(input())
    if now != 0 and now > maxN:
        maxN = now
print(maxN)
