from collections import defaultdict


def path1(filename):
    with open(filename) as f:
        fread = f.readlines()
        connects = defaultdict(list)
        for line in fread:
            x, y = line[:-1].split('-')
            connects[x].append(y)
            connects[y].append(x)

    routes = [['start']]
    smalls = [x for x in connects if x == x.lower() and x != 'end']
    ends = 0
    while True:
        for route in routes:
            cave = route[-1]
            for x in connects[cave]:
                if x == 'end':
                    ends += 1
                elif x not in smalls or x not in route:
                    routes.append(route + [x])
            routes.remove(route)
        if not routes:
            break
    print(ends)


def path2(filename):
    with open(filename) as f:
        fread = f.readlines()
        connects = defaultdict(list)
        for line in fread:
            x, y = line[:-1].split('-')
            connects[x].append(y)
            connects[y].append(x)

    routes = [['start']]
    smalls = [x for x in connects if x == x.lower() and x != 'end']
    ends = 0
    while True:
        newroutes = []
        for route in routes:
            cave = route[-1]
            for x in connects[cave]:
                if x == 'end':
                    ends += 1
                elif x not in smalls or x not in route:
                    newroutes.append(route + [x])
                elif x != 'start' and all([2 > route.count(y) for y in smalls]):
                    newroutes.append(route + [x])
        if not newroutes:
            break
        routes = newroutes.copy()
    print(ends)


path2('12-input.txt')
