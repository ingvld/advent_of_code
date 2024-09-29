
def non_overlapping_claim(filename):
    seen = {}

    overlapping_ids = set()
    ids = set()

    with open(filename) as f:
        for line in f.readlines():
            id, rectangle = line.split('@')
            ids.add(id)

            place, dims = map(lambda x: x.strip(),rectangle.split(':'))
            left,top = map(int, place.split(','))
            width, height = map(int, dims.split('x'))

            overlap_found = False
            
            for i in range(left,left+width):
                for j in range(top, top+height):
                    if (i, j) in seen:
                        if seen[(i,j)] not in overlapping_ids:
                            overlapping_ids.add(seen[i,j])
                        overlapping_ids.add(id)                        
                    else:
                        seen[(i,j)] = id
    
    print(ids.difference(overlapping_ids))

non_overlapping_claim('3-input')