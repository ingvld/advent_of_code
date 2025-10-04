import sys
from heapq import heappop, heappush


def increment_risk(ls, n):
    res = []
    for x in ls:
        nx = x+n

        print(x,n,nx)
        if nx > 9:
            nx = nx%9+1
        res.append(nx)
    return res
    
with open(sys.argv[1]) as f:
    grid = []

    for line in f.readlines():
        original_nums=list(map(int, line.strip()))
        new_nums=[]
        new_nums.extend(original_nums)
        for n in range(1,5):
            new_nums.extend(increment_risk(original_nums,n))
        grid.append(new_nums)

    orig_grid_len = len(grid)

    for n in range(1,5):
        for j in range(orig_grid_len):
            grid.append(increment_risk(grid[j],n))
            

with open("ng","w") as f:
    for line in grid:
        for x in line:
            f.write(str(x))
        f.write("\n")
print(grid[0])
print(len(grid[0]))
print(len("11637517422274862853338597396444961841755517295286"))
visited = {(0, 0)}
current = [(0, 0, 0)]
goal = (len(grid) - 1, len(grid[0]) - 1)
print("WOHOOO")
print(len(grid))

while goal not in visited:
    risk, x, y = heappop(current)

    for nx, ny in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
        if (nx, ny) in visited:   # previously visited
            continue
        if not (
            0 <= nx < len(grid) and 0 <= ny < len(grid[0])
        ):   # out of bounds
            continue

        new_risk = risk + grid[nx][ny]

        if (nx, ny) == goal:
            print(new_risk)

        visited.add((nx, ny))
        heappush(current, (new_risk, nx, ny))
