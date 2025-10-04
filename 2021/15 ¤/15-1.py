import sys
from heapq import heappop, heappush

with open(sys.argv[1]) as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

visited = {(0,0)}
current = [(0,0,0)]
goal=(len(grid)-1,len(grid[0])-1)

while goal not in visited:
    risk, x, y = heappop(current)

    for nx, ny in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
        if (nx, ny) in visited:   # previously visited
            continue
        if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):   # out of bounds
            continue

        new_risk = risk + grid[nx][ny]

        if (nx,ny)==goal:
            print(new_risk)

        visited.add((nx, ny))
        heappush(current,(new_risk, nx, ny))
