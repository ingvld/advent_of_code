import re

def oppg1(filename):
    total = 0

    with open(filename)  as f:
        pattern = '(([2-9]\d)|(\d\d\d+)|(1[5-9]))\ [rgb]|(14\ green)|(1[34]\ red)'
        for line in f.readlines():
            if not re.search(pattern,line):
                print(line)
                total += int(re.search(r'\d+',line).group())

    print(total)


def oppg2(filename):
    total = 0

    with open(filename) as f:

        for line in f.readlines():
            blue,red,green = 0,0,0

            elements = line.split()[2:]

            for i in range(0,len(elements),2):
                number, colour = int(elements[i]), elements[i+1].strip(';,')

                match colour:
                    case 'blue':
                        if number > blue:
                            blue = number
                    case 'red':
                        if number > red:
                            red = number
                    case 'green':
                        if number > green:
                            green = number
            total += red * blue * green
    
    print(total)
                    

oppg2('2-input')



