# Стоимость покупки
a = int(input())
b = int(input())
n = int(input())
cost = a * 100 + b
total = cost * n
print(total // 100, total % 100)
