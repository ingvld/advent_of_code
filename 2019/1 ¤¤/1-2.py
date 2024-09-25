with open('1-input.txt') as f:
    modules = [int(line.strip()) for line in f.readlines()]

def fuel_amount(current,rest):
    if rest <= 0:
        return current
    fuel_needed = max(0,rest // 3 - 2)
    return fuel_amount(current+fuel_needed,fuel_needed)

tot = 0

for module in modules:
    tot += fuel_amount(0,module)

print(tot)
