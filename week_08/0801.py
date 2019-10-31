print('0' in map(
    (lambda x:
     open('input.txt', 'r', encoding='utf8').read().strip().split('\n')[x]),
    range(1, 1 + int(open('input.txt', 'r', encoding='utf8').readline().strip()
            )
        )
    )
)