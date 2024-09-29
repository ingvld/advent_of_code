signals = {}
moves = []

def find(x):
    if x.isnumeric():
        return int(x)
    
    return False if x not in signals else signals[x]

with open('2015/7/7-test.txt') as f:
    for line in f.readlines():
        parts = line.strip().split()
        
        match len(parts):
            case 3:
                if type(find(parts[0])) == int:
                    signals[parts[2]] = find(parts[0])
                else:
                    moves.append(['TO',parts[0], parts[1]])
            case 4:
                moves.append([parts[0],parts[1],parts[3]])
            case 5:
                moves.append([parts[1],parts[2],parts[0],parts[4]])

def format_same_length(n1,n2):
    n1,n2 = str(bin(n1))[2:], str(bin(n2))[2:]
    len1,len2 = len(n1), len(n2)

    diff = abs(len1-len2)

    if len1 > len2:
        n2 = n2.zfill(len2+diff)
    elif diff:
        n1 = n1.zfill(len1+diff)

    return (n1,n2)

def bit_and(x,y):
    x,y = format_same_length(x,y)
    res = ''

    for i in range(len(x)):
        if x[i] == y[i] == '1':
            res += '1'
        else:
            res += '0'

    return(int(res,2))

def bit_or(x,y):
    x,y = format_same_length(x,y)
    res = ''

    for i in range(len(x)):
        if x[i] == y[i] == '0':
            res += '0'
        else:
            res += '1'

    return int(res,2)

def shift(dir, n, x):
    x = str(bin(x))[2:]
    n = int(n)

    if dir == 'l':
        x = x.ljust(len(x)+n,'0')
    else:
        x = x[:-n]

    return int(x,2)

def bit_not(x):
    x = str(bin(x))[2:]
    res = ''

    for y in x:
        if y == '0':
            res += '1'
        else:
            res += '0'
    
    return int(res.rjust(16,'1'),2)

i = 0

while i < 1000:
    unsolved = []
    
    for move in moves:
        match move[0]:
            case 'AND':
                wire1, wire2 = find(move[1]), find(move[2])
                if wire1 and wire2:
                    signals[move[3]] = bit_and(wire1, wire2)
                else:
                    unsolved.append(move)
            case 'OR':
                wire1, wire2 = find(move[1]), find(move[2])
                if wire1 and wire2:
                    signals[move[3]] = bit_or(wire1, wire2)
                else:
                    unsolved.append(move)
            case 'LSHIFT':
                wire = find(move[2])
                if wire:
                    signals[move[3]] = shift('l', move[1], wire)
                else:
                    unsolved.append(move)
            case 'RSHIFT':
                wire = find(move[2])
                if wire:
                    signals[move[3]] = shift('r', move[1], wire)
                else:
                    unsolved.append(move)
            case 'NOT':
                wire = find(move[1])
                if wire:
                    signals[move[2]] = bit_not(wire)
                else:
                    unsolved.append(move)
            case 'TO':
                wire = find(move[1])
                if wire:
                    signals[move[2]] = wire
                else:
                    unsolved.append(move)

    i += 1

    moves = unsolved

print(signals)
print(unsolved)