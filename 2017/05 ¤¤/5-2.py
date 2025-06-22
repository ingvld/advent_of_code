import sys

with open(sys.argv[1]) as f:
    instructions = list(map(int, f.readlines()))

i  = instructions[0]
steps = 0

while 0 <= i < len(instructions):
    j = instructions[i]
    instructions[i] += 1 if j < 3 else -1
    i += j
    steps += 1

print(steps)
    
