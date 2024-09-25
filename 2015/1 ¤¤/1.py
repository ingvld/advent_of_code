def floors1(filnavn):
    with open(filnavn) as f:
        moves = f.readline()[:-1]
    floor = 0
    for x in moves:
        floor += 1 if x == '(' else -1
    print(floor)


def floors2(filnavn):
    with open(filnavn) as f:
        moves = f.readline()[:-1]

    i, floor = 0, 0
    while floor >= 0 and i < len(moves):
        floor += 1 if moves[i] == '(' else -1
        i += 1
    print(i)


floors1('1/1-input.txt')
