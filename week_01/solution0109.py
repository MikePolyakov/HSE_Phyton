# Сумма цифр трехзначного числа
n = int(input())
n1 = n % 10
n2 = ((n - n % 10) // 10) % 10
n3 = n // 100
total = n1 + n2 + n3
print(total)
