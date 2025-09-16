import sys
from heapq import heappop, heappush

with open(sys.argv[1]) as f:
    grid = [line.strip() for line in f.readlines()]

visited = set()
current = []
    
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "a":
            visited.add((i,j))
            current.append((0,i,j,"a"))

done = False

while not done:
    dist, x, y, height = heappop(current)

    for nx, ny in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
        if (nx, ny) in visited:   # previously visited
            continue
        if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):   # out of bounds
            continue

        grid_val = grid[nx][ny]
        
        if ord(grid_val if grid_val!="E" else "z") - ord(height) > 1:   # too high above current pos
            continue

        if grid_val == "E":
            print(dist+1)
            done = True
            break

        visited.add((nx, ny))
        heappush(current, (dist + 1, nx, ny, grid_val))
