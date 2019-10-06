# пересечение событий 1
start1 = int(input())
finish1 = int(input())
start2 = int(input())
finish2 = int(input())
isS1in2 = start2 <= start1 <= finish2
isF1in2 = start2 <= finish1 <= finish2
isS2in1 = start1 <= start2 <= finish1
isF2in1 = start1 <= finish2 <= finish1
answer = isS1in2 or isF1in2 or isS2in1 or isF2in1
print(answer)
