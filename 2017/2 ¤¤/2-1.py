with open('2017\\2\\2-input.txt') as f:
    rows = [[int(y) for y in x.split()] for x in f.readlines()]

tot = 0

for row in rows:
    if len(row) > 1:
        high, low = row[0], row[0]
        for x in row[1:]:
            if x > high:
                high = x
            elif x < low:
                low = x
        tot += high-low

print(tot)
