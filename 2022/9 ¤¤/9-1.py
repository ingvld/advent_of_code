with open('9-test2.txt') as f:
    moves = [x.strip().split() for x in f.readlines()]



def is_adjacent():
    row, col = head[0],head[1]
    adjacents = [[x, y] for x in range(row-1,row+2) for y in range(col-1,col+2)]

    return tail in adjacents

def move_tail():
    for i in range(2):
        if tail[i] < head[i]:
            tail[i] += 1
        elif tail[i] > head[i]:
            tail[i] -= 1  


head,tail = ([0,0]),[0,0]
tail_visits = set(tuple(tail))

for move in moves:
    direction, steps = move[0], int(move[1])

    for i in range(steps):
        match direction:
            case 'R':
                head[0] += 1
            case 'L':
                head[0] -= 1
            case 'U':
                head[1] += 1
            case 'D':
                head[1] -= 1
        
        if not is_adjacent():
            move_tail()
            tail_visits.add(tuple(tail))

print(len(tail_visits))


        