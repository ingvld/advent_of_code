def octoflash1(filename):
    with open(filename) as f:
        octos = [list(map(int, line)) for line in f.read().splitlines()]
    step, flashcount = 0, 0
    while step < 100:
        flashes, flashed = [], []
        for i in range(len(octos)):
            for n in range(len(octos[i])):
                if octos[i][n] == 9:
                    flashes.append((i, n))
                    octos[i][n] = 0
                else:
                    octos[i][n] += 1
        while flashes:
            x, y = flashes[-1][0], flashes[-1][1]
            flashed.append((x, y))
            flashes.pop()
            adjacents = [(x+1, y+1), (x+1, y), (x+1, y-1), (x, y+1),
                         (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]
            for point in adjacents:
                p0, p1 = point[0], point[1]
                if p0 in range(len(octos)) and p1 in range(len(octos)):
                    if (p0, p1) not in flashes and (p0, p1) not in flashed:
                        if octos[p0][p1] == 9:
                            flashes.append((p0, p1))
                            octos[p0][p1] = 0
                        else:
                            octos[p0][p1] += 1
            flashcount += 1
        step += 1
    print(flashcount)


def octoflash2(filename):
    with open(filename) as f:
        octos = [list(map(int, line)) for line in f.read().splitlines()]
    step = 0
    while True:
        flashes, flashed = [], []
        for i in range(len(octos)):
            for n in range(len(octos[i])):
                if octos[i][n] == 9:
                    flashes.append((i, n))
                    octos[i][n] = 0
                else:
                    octos[i][n] += 1
        while flashes:
            x, y = flashes[-1][0], flashes[-1][1]
            flashed.append((x, y))
            flashes.pop()
            adjacents = [(x+1, y+1), (x+1, y), (x+1, y-1), (x, y+1),
                         (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]
            for point in adjacents:
                p0, p1 = point[0], point[1]
                if p0 in range(len(octos)) and p1 in range(len(octos)):
                    if (p0, p1) not in flashes and (p0, p1) not in flashed:
                        if octos[p0][p1] == 9:
                            flashes.append((p0, p1))
                            octos[p0][p1] = 0
                        else:
                            octos[p0][p1] += 1
        step += 1
        if len(flashed) == len(octos) * len(octos[0]):
            print(step)
            break


octoflash2('11-input.txt')
