import re

# del1
'''def vents(inputfil):
    with open(inputfil) as data:
        coords = [tuple(map(int, (x1, y1, x2, y2))) for x1, y1, x2, y2 in [re.split(',| -> ', line)
                  for line in data.read().splitlines()]]
    points, overlaps = set(), set()
    for x1, y1, x2, y2 in coords:
        diff = abs(x1-x2) if x1 != x2 else abs(y1-y2)
        if x1 == x2:
            n = min(y1, y2)
            for i in range(diff+1):
                if (x1, n+i) in points:
                    overlaps.add((x1, n+i))
                else:
                    points.add((x1, n+i))

        if y1 == y2:
            n = min(x1, x2)
            for i in range(diff+1):
                if (n+i, y1) in points:
                    overlaps.add((n+i, y1))
                else:
                    points.add((n+i, y1))
    print(len(overlaps))'''


# del 2
def vents(inputfil):
    with open(inputfil) as data:
        coords = [tuple(map(int, (x1, y1, x2, y2))) for x1, y1, x2, y2 in [re.split(',| -> ', line)
                  for line in data.read().splitlines()]]
    points, overlaps = set(), set()
    for x1, y1, x2, y2 in coords:
        i, diff = 0, abs(x1-x2) if x1 != x2 else abs(y1-y2)
        while i < diff + 1:
            x = x1 if x1 == x2 else x1 + i if x1 < x2 else x1 - i
            y = y1 if y1 == y2 else y1 + i if y1 < y2 else y1 - i
            if (x, y) not in points:
                points.add((x, y))
            elif (x, y) not in overlaps:
                overlaps.add((x, y))
            i += 1
    print(len(overlaps))


vents('5-input.txt')
