# Цвет клеток шахматной доски
col_1 = int(input())
raw_1 = int(input())
col_2 = int(input())
raw_2 = int(input())
if (col_1 % 2 != 0 and raw_1 % 2 != 0) or (col_1 % 2 == 0 and raw_1 % 2 == 0):
    set_1 = 1
if (col_2 % 2 != 0 and raw_2 % 2 != 0) or (col_2 % 2 == 0 and raw_2 % 2 == 0):
    set_2 = 1
if (col_1 % 2 != 0 and raw_1 % 2 == 0) or (col_1 % 2 == 0 and raw_1 % 2 != 0):
    set_1 = 0
if (col_2 % 2 != 0 and raw_2 % 2 == 0) or (col_2 % 2 == 0 and raw_2 % 2 != 0):
    set_2 = 0
if set_1 == set_2:
    print('YES')
else:
    print('NO')
