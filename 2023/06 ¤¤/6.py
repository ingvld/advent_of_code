from math import sqrt, floor

def oppg1(filename):
    with open(filename) as f:
        races = zip(map(int,f.readline().split(':')[1].split()),
                    map(int,f.readline().split(':')[1].split()))
        
    total = 1

    for time,distance in races:
        score_gap = time**2//4-(distance+1)

        if time % 2:
            total *= (-1 + sqrt(1 + 4*score_gap))//2 * 2 + 2
        else:
            total *= floor(sqrt(score_gap)) * 2 + 1

    print(total)

def oppg2(filename):
    with open(filename) as f:
        time = int(''.join(f.readline().split()[1:]))
        distance = int(''.join(f.readline().split()[1:]))

    score_gap = time**2//4-(distance+1)

    if time % 2:
        print((-1 + sqrt(1 + 4*score_gap))//2 * 2 + 2)
    else:
        print(floor(sqrt(score_gap)) * 2 + 1)

oppg2('6-input.txt')