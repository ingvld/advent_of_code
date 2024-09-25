# del1
def lowpoints1(filnavn):
    with open(filnavn) as f:
        points = [list(map(int, x)) for x in f.read().splitlines()]
    risk = 0
    for i in range(len(points)):
        for n in range(len(points[i])):
            left = points[i][n-1] if n else 9
            up = points[i-1][n] if i else 9
            right = points[i][n+1] if n < len(points[i])-1 else 9
            down = points[i+1][n] if i < len(points)-1 else 9
            if all(x > points[i][n] for x in [left, up, right, down]):
                risk += points[i][n] + 1
    print(risk)


# del2


def lowpoints2(filnavn):
    with open(filnavn) as f:
        points = f.read().splitlines()
    basins = []
    for i in range(len(points)):
        groups = []
        n, s = 0, set()
        while n < len(points[i]):
            if points[i][n] != '9':
                s.add((i, n))
                n += 1
                if n == len(points[i]):
                    groups.append(s)
            else:
                if s:
                    groups.append(s)
                    s = set()
                n += 1
        for group in groups:
            added = 0
            for point in group:
                for basin in basins:
                    if (point[0]-1, point[1]) in basin:
                        basin.update(group)
                        if added and added != basin:
                            basin.update(basins[basins.index(added)])
                            del basins[basins.index(added)]
                        added = basin
            if not added:
                basins.append(group)
    bigthree = sorted([len(x) for x in basins])[-3:]
    print(bigthree[0] * bigthree[1] * bigthree[2])


lowpoints2('9-input.txt')
