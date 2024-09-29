def naughty_or_nice1(filnavn):
    with open(filnavn) as f:
        string_list = f.read().splitlines()
    nicecount = 0
    for string in string_list:
        if 'ab' not in string and 'cd' not in string and 'pq' not in string and 'xy' not in string:
            vowelcount, double, lastchar = 0, 0, 0
            for x in string:
                if x in 'aeiou':
                    vowelcount += 1
                if x == lastchar:
                    double = 1
                lastchar = x
            if vowelcount > 2 and double:
                nicecount += 1
    print(nicecount)


def naughty_or_nice2(filnavn):
    with open(filnavn) as f:
        string_list = f.read().splitlines()
    nicecount = 0
    for string in string_list:
        pair, repeat = 0, 0
        lastchar, lastlastchar = 0, 0
        pairs = []
        for i in range(len(string)):
            if string[i] == lastlastchar:
                repeat = 1
            lastlastchar, lastchar = lastchar, string[i]
            if i > 0:
                twos = string[i-1:i+1]
                print(twos)
                if twos in pairs[:-1]:
                    pair = 1
                else:
                    pairs.append(twos)
        if pair and repeat:
            nicecount += 1

    print(nicecount)


naughty_or_nice2('5/5-input.txt')
