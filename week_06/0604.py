# сортировка подсчетом
marks = map(int, input().split())
cntMarks = [0] * 11
print(cntMarks)
for mark in marks:
    cntMarks[mark] += 1
    print(mark, cntMarks[mark])
for nowMark in range(11):
    print((str(nowMark) + ' ') * cntMarks[nowMark], end='')
