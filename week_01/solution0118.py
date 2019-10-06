# Электронные часы-2
n = int(input())
sec10 = str(n % 60 // 10)
sec1 = str(n % 60 % 10)
sec = sec10 + sec1
minute = ((n - n % 60) // 60) % 60
min10 = minute // 10
min1 = minute % 10
minStr = str(min10) + str(min1)
hour = ((n - n % 60) // 3600) % 24
print(hour, minStr, sec, sep=':')
