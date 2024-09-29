import numpy as np

with open('2022\8\8-input.txt') as f:
    trees = np.array([[int(x) for x in line.strip()] for line in f.readlines()])

def find_views(line, tree, i):
    lefts = 0
    for x in line[i-1::-1]:
        lefts += 1
        if x >= tree:
            break

    rights = 0

    for x in line[i+1:]:
        rights += 1
        if x >= tree:
            break

    return lefts * rights

max_score = 0

for i in range(1,len(trees)-1):
    row = trees[i]
    for n in range(1,len(row)-1):
        col = trees[:,n]
        tree = row[n]

        score = find_views(row, tree, n) * find_views(col, tree, i)
        if score > max_score:
            max_score = score

print(max_score)