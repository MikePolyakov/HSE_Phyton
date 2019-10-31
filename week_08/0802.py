# ввод n чисел с клавиатуры
t = list(map(
    lambda x: int(input()),
    range(
        int(input())
        )
    ))
print(*t)
print(type(t))
mset = set(t)

print(0 in mset)
