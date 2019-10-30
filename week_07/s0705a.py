n = int(input())
yes_set = set(range(1, n + 1))
while True:
    input_line = input()
    if input_line == 'HELP':
        break
    else:
        input_set = set(map(int, input_line.split()))
        yes_no_answer = input()
        if yes_no_answer == "YES":
            yes_set &= input_set
        elif yes_no_answer == "NO":
            yes_set -= input_set
        elif len(yes_set) == 1:
            break
print(*sorted(yes_set))
