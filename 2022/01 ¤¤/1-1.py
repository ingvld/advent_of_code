with open('2022\\1\\1-input.txt') as cals:
    vals = cals.readlines()

high = 0
cur = 0

for x in vals:
    if x != '\n':
        cur += int(x)
    else:
        if cur > high:
            high = cur
        cur = 0
        
print (high) if high > cur else print(cur)