import sys

with open(sys.argv[1]) as f:
    instructions = list(map(int, f.readlines()))

i  = instructions[0]
steps = 0

while 0 <= i < len(instructions):
    instructions[i] += 1
    i += instructions[i]-1
    steps += 1

print(steps)
    
