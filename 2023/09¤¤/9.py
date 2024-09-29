def oppg1(filename):

    def find_next(sequence):
        if not any(sequence):
            return 0
    
        return sequence[-1] + find_next([sequence[i]-sequence[i-1]
                                         for i in range(1,len(sequence))])
    
    total = 0
    
    with open(filename) as f:
        for line in f.readlines():
            total += find_next(list(map(int,line.split())))

    print(total)


def oppg2(filename):

    def find_prev(sequence):
        if not any(sequence):
            return 0
    
        return sequence[0] - find_prev([sequence[i]-sequence[i-1]
                                        for i in range(1,len(sequence))])
    
    total = 0
    
    with open(filename) as f:
        for line in f.readlines():
            total += find_prev(list(map(int,line.split())))

    print(total)

oppg2('9-input.txt')

    
