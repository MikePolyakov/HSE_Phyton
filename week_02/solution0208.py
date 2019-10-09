# Шоколадка
n = int(input())
m = int(input())
k = int(input())
if (n == 1 or m == 1) and (k <= n * m):
    print('YES')
elif (k % n == 0 or k % m == 0) and (k <= n * m):
    print('YES')
else:
    print('NO')
