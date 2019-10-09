# Шашки
col_1 = int(input())
raw_1 = int(input())
col_2 = int(input())
raw_2 = int(input())

if (col_2 % 2 != 0 and raw_2 % 2 != 0) or (col_2 % 2 == 0 and raw_2 % 2 == 0):
    if abs(col_2 - col_1) <= (raw_2 - raw_1):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
