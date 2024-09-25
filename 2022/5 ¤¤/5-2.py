import re

with open('2022\\5\\5-input.txt') as f:
    lines = f.readlines()

number_of_cols = len(lines[0]) // 4
stacks = [[] for i in range(number_of_cols)]
    
i = 0

while lines[i][1] != '1':
    line = lines[i]

    for n in range(number_of_cols):
        letter = line[n*4+1]
        if letter != ' ':
            stacks[n].append(letter)

    i += 1
    
moves = []

for line in lines[i+2:]:
    moves.append(list(map(int,re.split(' from | to |\n',line.strip()[5:]))))

for move in moves:
    amount, from_stack, to_stack = move[0], 1, stacks[move[2]-1]
    stacks[move[2]-1] = stacks[move[1]-1][:move[0]] + stacks[move[2]-1]
    del stacks[move[1]-1][:move[0]]

res = ''

for stack in stacks:
    res += stack[0]

print(res)