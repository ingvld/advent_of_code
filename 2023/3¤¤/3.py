
def oppg1(filename):
    with open(filename) as f:
        fread = f.readlines()

    symbol_adjecents = set()

    for i in range(len(fread)):
        for n in range(len(fread[i])):
            if fread[i][n] not in '0123456789.\n':
                for x in range(i-1,i+2):
                    for y in range(n-1,n+2):
                        symbol_adjecents[(x,y)]
    
    total = 0
    number = ''
    num_found = False

    for i in range(len(fread)):
        for n in range(len(fread[i])):
            if fread[i][n] in '0123456789':
                number += fread[i][n]
                if (i,n) in symbol_adjecents:
                    num_found = True
            else:
                if number and num_found:
                    total += int(number)
                number = ''
                num_found = False
    
    print(total)

def oppg2(filename):
    with open(filename) as f:
        fread = f.readlines()

    number_at_position = {}

    for i in range(len(fread)):
        number = ''
        positions = []

        for n in range(len(fread[i])):
            if fread[i][n] in '1234567890':
                number += fread[i][n]
                positions.append((i,n))
            else:
                if number:
                    for pos in positions:
                        number_at_position[pos] = int(number)
                number = ''
                positions = []
                
    
    total = 0
    number = ''

    num_found_gear = set()

    for i in range(len(fread)):
        for n in range(len(fread[i])):
            if fread[i][n] == '*':
                first_num = 0

                for x in range(i-1,i+2):
                    found_at_line = False
                    for y in range(n-1,n+2):
                        if (x,y) in number_at_position:
                            if first_num:
                                if not found_at_line or fread[x][n] not in '1234567890':
                                    total += int(number_at_position[(x,y)]) * first_num

                            first_num = number_at_position[(x,y)]
                            found_at_line = True
                
                first_num = 0
    print(total)


oppg2('3-input')