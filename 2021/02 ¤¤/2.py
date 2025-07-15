with open('2-input.txt') as course:
    route = [(x, int(y)) for x, y in [x.split() for x in course.read().splitlines()]]

'''hor, dep = 0, 0
for x in route:
    if x[0] == 'forward':
        hor += x[-1]
    elif x[0] == 'down':
        dep += x[-1]
    else:
        dep -= x[-1]'''

aim, hor, dep = 0, 0, 0
for x in route:
    if x[0] == 'forward':
        hor += x[-1]
        dep += aim*x[-1]
    elif x[0] == 'down':
        aim += x[-1]
    else:
        aim -= x[-1]

print(hor * dep)

print(0b00100 + 0b11110)
