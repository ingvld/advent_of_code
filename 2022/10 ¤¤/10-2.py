with open('10-input.txt') as f:
    instructs = [x.strip().split() for x in f.readlines()]

cycle,row = 0, 0
x = 1
crt = ['' for i in range(6)]

def increment_cycle(n=1):
    global cycle,row
    cycle += 1
    if cycle > 40:
        cycle -= 40
        row += 1
    
    symbol = ' '
    print(cycle, x)
    if cycle-1 in [x-1,x,x+1]:
        symbol = '▓'
    
    crt[row] += symbol


for instruct in instructs:
    if instruct[0] == 'noop':
        increment_cycle()
        continue
    increment_cycle()
    increment_cycle()
    x += int(instruct[1])

for line in crt:
    print(line)