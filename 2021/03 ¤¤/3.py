with open('3-input.txt') as diagnostic:
    diags = [x for x in diagnostic.read().splitlines()]

'''bits = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
        [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

for x in diags:
    i = 0
    while i < len(x):
        bits[i][int(x[i])] += 1
        i += 1

gamma, epsilon = '', ''
for x in bits:
    gamma += '0' if x[0] < x[1] else '1'
    epsilon += '1' if x[0] < x[1] else '0'''

# del2
oxygen, co2 = diags.copy(), diags.copy()
i = 0
while len(oxygen) != 1:
    c0nt, c1nt = 0, 0
    for x in oxygen:
        if x[i] == '0':
            c0nt += 1
        else:
            c1nt += 1
    if c0nt > c1nt:
        for x in diags:
            if x in oxygen and x[i] == '1':
                oxygen.remove(x)
    else:
        for x in diags:
            if x in oxygen and x[i] == '0':
                oxygen.remove(x)
    i += 1

i = 0
while len(co2) != 1:
    c0nt, c1nt = 0, 0
    for x in co2:
        if x[i] == '0':
            c0nt += 1
        else:
            c1nt += 1
    if c1nt < c0nt:
        for x in diags:
            if x in co2 and x[i] == '0':
                co2.remove(x)
    else:
        for x in diags:
            if x in co2 and x[i] == '1':
                co2.remove(x)
    i += 1

print(int(oxygen[0], 2) * int(co2[0], 2))
