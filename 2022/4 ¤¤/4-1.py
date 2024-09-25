with open('2022\\4\\4-input.txt') as f:
    pairs = [[list(map(int,z.split('-'))),list(map(int,y.split('-')))] for z,y in [x.split(',') for x in f.readlines()]]

res = 0
for x,y in pairs:
    if x[0] <= y[0] and x[1] >= y[1] or y[0] <= x[0] and y[1] >= x[1]:
        res += 1

print(res)