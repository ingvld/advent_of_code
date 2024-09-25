import heapq

PIPES = {'|':'NS','-':'EW','L':'NE','J':'NW','7':'SW','F':'SE','.':''}
NEW_DIRECTION = {'N':'S','E':'W','W':'E','S':'N'}
MOVES = {'N':(-1,0),'E':(0,+1),'W':(0,-1),'S':(+1,0)}

def oppg1(filename):

    with open(filename) as f:
        grid = [line.strip() for line in f.readlines()]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    start = (i,j)

        ones = []

        for direction,move in MOVES.items():
            if NEW_DIRECTION[direction] in PIPES[grid[move[0]+start[0]][move[1]+start[1]]]:
                ones.append((move[0]+start[0],move[1]+start[1]))
                ones.append(NEW_DIRECTION[direction])

    def get_new_direction(pos,from_dir):
        pipe_direction = PIPES[grid[pos[0]][pos[1]]]
        return pipe_direction[0] if pipe_direction[0] != from_dir else pipe_direction[1]
    
    def find_furthest(p1,p1_from,p2,p2_from):
        
        steps = 1

        while p1 != p2:
            p1_dir,p2_dir = get_new_direction(p1,p1_from),get_new_direction(p2,p2_from)
            p1_move,p2_move = MOVES[p1_dir],MOVES[p2_dir]

            p1,p2 = (p1_move[0]+p1[0],p1_move[1]+p1[1]),(p2_move[0]+p2[0],p2_move[1]+p2[1])
            p1_from,p2_from = NEW_DIRECTION[p1_dir],NEW_DIRECTION[p2_dir]

            steps += 1

        return steps
    print(find_furthest(*ones))

def oppg2(filename):

    with open(filename) as f:
        grid = [line.strip() for line in f.readlines()]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    start = (i,j)

        for direction,move in MOVES.items():
            if NEW_DIRECTION[direction] in PIPES[grid[move[0]+start[0]][move[1]+start[1]]]:
                nxt,nxt_from = (move[0]+start[0],move[1]+start[1]),NEW_DIRECTION[direction]
                break

    def get_new_direction(pos,from_dir):
        pipe_direction = PIPES[grid[pos[0]][pos[1]]]
        return pipe_direction[0] if pipe_direction[0] != from_dir else pipe_direction[1]
    
    loop = {start[0]:[]}
    steps = 1
    prev0 = start[0]
    arr = [start[1]]
    
    while nxt != start:
        if nxt[0] == prev0:
            arr.append(nxt[1])
        else:
            if prev0 not in loop:
                loop[prev0] = []
            heapq.heappush(loop[prev0],(min(arr[0],arr[-1]),max(arr[0],arr[-1])))
            
            prev0 = nxt[0]
            arr = [nxt[1]]

        nxt_dir = get_new_direction(nxt,nxt_from)
        nxt_move = MOVES[nxt_dir]
        nxt,nxt_from = (nxt_move[0]+nxt[0],nxt_move[1]+nxt[1]),NEW_DIRECTION[nxt_dir]

        steps += 1
    
    print(loop)

    betweens = 0

    for line in loop.values():
        prev = None

        while line:
            current = heapq.heappop(line)
            if prev:
                print(current[0],prev)
                betweens += abs(current[0]-prev-1)
                prev = None
            else:
                prev = current[1]

    print(betweens)


oppg2('10-test-2.txt')