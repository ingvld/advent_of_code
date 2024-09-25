def folds1(filename):
    with open(filename) as f:
        pointlines, foldlines = [x.split('\n') for x in f.read().split('\n\n')]
        points, folds = [], []
        for line in pointlines:
            x, y = line.split(',')
            points.append([int(x), int(y)])
        for line in foldlines:
            if line:
                fold_descript, number = line.split('=')
                dimension = 0 if fold_descript[-1] == 'x' else 1
                folds.append([dimension, int(number)])

    postfoldpoints = set()
    for fold in folds:
        dim, num = fold[0], fold[1]
        for point in points:
            if point[dim] > num:
                point[dim] -= (point[dim] - num) * 2
            postfoldpoints.add(tuple(point))
        break
    print(len(postfoldpoints))


def folds2(filename):
    with open(filename) as f:
        pointlines, foldlines = [x.split('\n') for x in f.read().split('\n\n')]
        points, folds = [], []
        for line in pointlines:
            x, y = line.split(',')
            points.append([int(x), int(y)])
        for line in foldlines:
            if line:
                fold_descript, number = line.split('=')
                dimension = 0 if fold_descript[-1] == 'x' else 1
                folds.append([dimension, int(number)])

    for fold in folds:
        newpoints = []
        dim, num = fold[0], fold[1]
        for point in points:
            if point[dim] > num:
                point[dim] -= (point[dim] - num) * 2
            if point not in newpoints:
                newpoints.append(point)
        points = newpoints.copy()

    # visualizing
    import numpy as np

    xmax, ymax = 0, 0
    for point in points:
        if point[0] > xmax:
            xmax = point[0]
        if point[1] > ymax:
            ymax = point[1]

    img = np.zeros((ymax+1, xmax+1))

    for point in points:
        x, y = point[0], point[1]
        img[y][x] = 1

    print(img)


folds2('13-input.txt')
