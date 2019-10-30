import sys
words = set()

for line in sys.stdin.readlines():
    print(len(set(str(sys.stdin.read()).split(' '))))


print(type(line))
print(len(line))
print(line)