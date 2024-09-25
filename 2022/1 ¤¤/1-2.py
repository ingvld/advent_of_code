with open('2022\\1\\1-input.txt') as cals:
    vals = cals.readlines()

highs = [0, 0, 0]
cur = 0
ln = len(vals)

for n in range(ln):
    val = vals[n]
    if val != '\n':
        cur += int(val)

    if val == '\n' or n == ln-1:
        if cur > highs[0]:
            highs[0] = cur
            highs.sort()
        cur = 0

print(sum(highs))