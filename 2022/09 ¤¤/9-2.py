with open('9-input.txt') as f:
    moves = [x.strip().split() for x in f.readlines()]

def is_adjacent(k1, k2):
    row, col = k1[0],k1[1]
    adjacents = [[x, y] for x in range(row-1,row+2) for y in range(col-1,col+2)]

    return k2 in adjacents

def move_tail(knot_index):
    for i in range(2):
        if knots[knot_index][i] < knots[knot_index-1][i]:
            knots[knot_index][i] += 1
        elif knots[knot_index][i] > knots[knot_index-1][i]:
            knots[knot_index][i] -= 1  

knots = [[0,0] for x in range(10)]

tail_visits = set([tuple(knots[9])])

for move in moves:
    direction, steps = move[0], int(move[1])

    for i in range(steps):
        match direction:
            case 'R':
                knots[0][0] += 1
            case 'L':
                knots[0][0] -= 1
            case 'U':
                knots[0][1] += 1
            case 'D':
                knots[0][1] -= 1

        for i in range(1, 10):
            if not is_adjacent(knots[i-1], knots[i]):
                move_tail(i)
        tail_visits.add(tuple(knots[9]))

print(len(tail_visits))
