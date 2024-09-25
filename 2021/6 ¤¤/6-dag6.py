# del 1

'''def lanterns(inputfile):
    with open(inputfile) as f:
        fish = [int(x) for x in f.readline().split(',')]
    day = 0
    while day < 80:
        for i in range(len(fish)):
            if fish[i]:
                fish[i] -= 1
            else:
                fish[i] = 6
                fish.append(8)
        day += 1
    print(len(fish))


lanterns('6-input.txt')'''

# del 2


def lanterns(inputfile):
    with open(inputfile) as f:
        fread = f.read()
        fish = [fread.count(str(x)) for x in range(9)]
    day = 0
    while day < 256:
        state = fish.copy()
        for i in range(9):
            fish[i-1] += state[i]
            fish[i] -= state[i]
        fish[6] += state[0]
        day += 1
    print(sum(fish))


lanterns('6-input.txt')
