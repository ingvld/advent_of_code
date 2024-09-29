import numpy as np

with open('2022\8\8-input.txt') as f:
    trees = np.array([[int(x) for x in line.strip()] for line in f.readlines()])

invisibles = 0

for i in range(1,len(trees)-1):
    row = trees[i]
    for n in range(1,len(row)-1):
        tree = row[n]
        col = trees[:,n]
        if max(row[:n]) >= tree and max(row[n+1:]) >= tree:
            if max(col[:i]) >= tree and max(col[i+1:]) >= tree:
                invisibles += 1

number_of_trees = len(trees) * len(trees[0])
print(number_of_trees - invisibles)
