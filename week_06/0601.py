# Сортировка списков

myList = list(map(int, input().split()))
myList.sort()
print(' '.join(map(str, myList)))

myList = list(map(int, input().split()))
sortedList = sorted(myList)
print(' '.join(map(str, sortedList)))

print(sorted((1, 3, 2)))
print(sorted(range(10, -1, -2)))
print(sorted("cba"))