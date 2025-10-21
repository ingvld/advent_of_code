import sys
from heapq import heappop, heappush


def increment_risk(ls, n):
    res = []
    for x in ls:
        nx = x + n
        if nx > 9:
            nx = nx % 9
        res.append(nx)
    return res


with open(sys.argv[1]) as f:
    grid = []
    for line in f.readlines():
        original_nums = list(map(int, line.strip()))
        new_nums = []
        new_nums.extend(original_nums)
        for n in range(1, 5):
            new_nums.extend(increment_risk(original_nums, n))
        grid.append(new_nums)

    orig_grid_len = len(grid)
    for n in range(1, 5):
        for j in range(orig_grid_len):
            grid.append(increment_risk(grid[j], n))


visited = {(0, 0)}
current = [(0, 0, 0)]
goal = (len(grid) - 1, len(grid[0]) - 1)

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
