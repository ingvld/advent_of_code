with open('10-input.txt') as f:
    instructs = [x.strip().split() for x in f.readlines()]

cycle = 0
x = 1
signal_strenghts = []

def increment_cycle(n=1):
    global cycle
    cycle += 1
    
    if cycle in [20,60,100,140,180,220]:
        signal_strenghts.append(x*cycle)

for instruct in instructs:
    if instruct[0] == 'noop':
        increment_cycle()
        continue
    increment_cycle()
    increment_cycle()
    x += int(instruct[1])

print(sum(signal_strenghts))

