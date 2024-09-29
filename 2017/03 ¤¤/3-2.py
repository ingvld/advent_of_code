circle = 0

def find_next(pos):
    global circle
    x,y = pos

    if pos == (0,0) or pos == (-circle,-circle):
        circle += 1
        return (x+1,y)

    if x == circle and y < circle:
        return (x,y+1)

    if y == circle and x > -circle:
        return (x-1,y)
    
    if x == -circle and y > -circle:
        return (x,y-1)

    return (x+1,y)


def find_value(pos):
    x,y = pos

    tot = 0

    for i in range(x-1,x+2):
        for n in range(y-1,y+2):
            if (i,n) in position_values:
                tot += position_values[(i,n)]

    return tot

position_values = {(0,0):1}


value = 1
position = (0,0)

while value < 361527:
    position = find_next(position)
    value = find_value(position)

    position_values[position] = value

print(value)

