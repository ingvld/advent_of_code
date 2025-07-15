right,down = 0,0
coords = []

areas = {}

with open('6-test') as f:
    i = 0

    for line in f.readlines():
        x,y = map(int, line.split(','))
        coords.append((x,y))
        areas[(x,y)] = 0

        if x >= right:
            right = x+1
        if y >= down:
            down = y+1

for i in range(right):
    for j in range(down):
        lowest_difference = None
        coord_of_difference = None

        for coord in coords:
            difference = abs((i-coord[0]) + (2-coord[0]))
            print(difference)
            if lowest_difference is None or difference < lowest_difference:
                lowest_difference = difference
                coord_of_difference = coord
            elif lowest_difference == difference:
                coord_of_difference = None
        
        if coord_of_difference is not None:
            if i in (0,right-1) or j in (0,down-1):
                areas[coord_of_difference] = None
            else:
                print(areas[coord_of_difference])
                if areas[coord_of_difference] is not None:
                    areas[coord_of_difference] += 1

print(areas)
                

        
                


