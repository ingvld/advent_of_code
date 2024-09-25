def delivery1(filnavn):
    with open(filnavn) as f:
        moves = f.readline()[:-1]
    houses = {(0, 0)}
    housecount = 1
    ns, ew = 0, 0
    for x in moves:
        if x in '^v':
            ns += 1 if x == '^' else -1
        else:
            ew += 1 if x == '>' else -1
        if (ns, ew) not in houses:
            housecount += 1
            houses.add((ns, ew))
    print(housecount)


def delivery2(filnavn):
    with open(filnavn) as f:
        moves = f.readline()[:-1]
    houses, housecount = {(0, 0)}, 1
    north_east = [[0, 0], [0, 0]]
    move = 0
    for x in moves:
        coords = north_east[move % 2]
        if x in '^v':
            coords[0] += 1 if x == '^' else -1
        else:
            coords[1] += 1 if x == '>' else -1
        if tuple(coords) not in houses:
            housecount += 1
            houses.add(tuple(coords))
        move += 1

    print(housecount)


delivery2('3/3-input.txt')
