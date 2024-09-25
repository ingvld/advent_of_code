def opgg1(filename):

    with open(filename) as f:
        lines = f.readlines()

        galaxies = []

        i = 0
        offset = 0
        size_of_empty_area = 0

        while i < len(lines):
            galaxy_found = False

            j = 0
            while j < len(lines[i]):
                if lines[i][j] == '#':
                    galaxy_found = True

                    if size_of_empty_area:
                        offset += size_of_empty_area * 2
                    
                    galaxies.append((i+offset,j))

            if not galaxy_found:
                size_of_empty_area += 1
            i += 1

