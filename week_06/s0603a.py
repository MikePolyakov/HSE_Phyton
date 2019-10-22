S, N = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))
a.sort()
n = 0
i = 0
while (n < S):
    n += a[i]
    if(n<=S):
        i += 1
print(i)