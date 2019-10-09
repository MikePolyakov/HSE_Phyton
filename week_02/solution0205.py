# Ход короля
col_1 = int(input())
raw_1 = int(input())
col_2 = int(input())
raw_2 = int(input())

if abs(col_1 - col_2) == 1 and abs(raw_1 - raw_2) == 0:
    print('YES')
elif abs(col_1 - col_2) == 0 and abs(raw_1 - raw_2) == 1:
    print('YES')
elif abs(col_1 - col_2) == 1 and abs(raw_1 - raw_2) == 1:
    print('YES')
else:
    print('NO')
