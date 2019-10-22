
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b
n = 1
while n < len(c):
    for i in range(len(c) - n):
        if c[i] > c[i + 1]:
            c[i], c[i + 1] = c[i + 1], c[i]
    n += 1
print(*c)

