with open('3-test1.txt') as f:
    wires = [[(x[0],int(x[1:])) for x in line.strip().split(',')] for line in f.readlines()]

coords = set()
closest_intersection = None

for wire in wires:
    x,y = 0,0

    for move in wire:
        for i in range(move[1]):
            match move[0]:
                case 'R':
                    x += 1
                case 'L':
                    x -= 1
                case 'U':
                    y += 1
                case 'D':
                    y -= 1
            if (x,y) in coords:
                distance = abs(x) + abs(y)
                if not closest_intersection or distance < closest_intersection:
                    closest_intersection = distance
            coords.add((x,y))

print(closest_intersection)
                




