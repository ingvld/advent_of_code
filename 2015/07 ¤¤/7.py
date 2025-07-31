import sys

instructs = {}

with open(sys.argv[1]) as f:
    for line in f.readlines():
        signal, wire = line.strip().split(' -> ')
        instructs[wire] = signal

solved = {}

def get_signal(wire):
    if wire.isdigit():
        return int(wire)

    if wire not in solved:
        match instructs[wire].split():
            case [x]:
                solved[wire] = int(x) if x.isdigit() else get_signal(x)
            case [w1, 'AND', w2]:
                solved[wire] = get_signal(w1) & get_signal(w2)
            case [w1, 'OR', w2]:
                solved[wire] = get_signal(w1) | get_signal(w2)
            case [w1, 'LSHIFT', n]:
                solved[wire] = get_signal(w1) << int(n)
            case [w1, 'RSHIFT', n]:
                solved[wire] = get_signal(w1) >> int(n)
            case ['NOT', w1]:
                solved[wire] = ~get_signal(w1) & 65535

    return solved[wire]

if 'test' in sys.argv[1]:
    for x in instructs:
        print(f'{x}: {get_signal(x)}')
else:
    print(get_signal('a'))
