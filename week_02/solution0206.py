# Квартиры
x = int(input())
y = int(input())
if y % (y - x + 1) == 0 and (x - 1) % (y - x + 1) == 0:
    print('YES')
else:
    print('NO')
