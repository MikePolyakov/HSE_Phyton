# Точная степень двойки
'''
Дано натуральное число N.
Выведите слово YES, если число N является точной степенью двойки,
или слово NO в противном случае.
Операцией возведения в степень пользоваться нельзя!
'''
n = int(input())
result = 1
while result <= n:
    if n == result:
        print('YES')
        break
    else:
        result = result * 2
        if result > n:
            print('NO')
            break
