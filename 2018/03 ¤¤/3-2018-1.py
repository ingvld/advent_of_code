
def find_overlaps(filename):
    seen = set()
    doubles = set()

    with open(filename) as f:
        for line in f.readlines():
            place, dims = map(lambda x: x.strip(),line.split('@')[1].split(':'))
            left,top = map(int, place.split(','))
            width, height = map(int, dims.split('x'))
            
            for i in range(left,left+width):
                for j in range(top, top+height):
                    if (i, j) in seen:
                        doubles.add((i,j))
                    else:
                        seen.add((i,j))
    print(len(doubles))


find_overlaps('3-input')