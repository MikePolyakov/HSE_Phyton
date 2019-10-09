# Коровы
"""
n коров", если 10 < n < 20 или последняя цифра n - одна из 0, 5, 6, 7, 8, 9.
"n корова", если последняя цифра n == 1.
"n коровы" во всех остальных случаях.
"""
n = int(input())
if 10 <= n <= 20:
    print(n, 'korov')
elif n - (n // 10) * 10 == 0:
    print(n, 'korov')
elif n - (n // 10) * 10 == 5:
    print(n, 'korov')
elif n - (n // 10) * 10 == 6:
    print(n, 'korov')
elif n - (n // 10) * 10 == 7:
    print(n, 'korov')
elif n - (n // 10) * 10 == 8:
    print(n, 'korov')
elif n - (n // 10) * 10 == 9:
    print(n, 'korov')
elif n - (n // 10) * 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
