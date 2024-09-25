import statistics

# del 1


def crabs1(inputfile):
    with open(inputfile) as f:
        crabbies = list(map(int, f.readline().split(',')))
    med = statistics.median(crabbies)
    print(sum(abs(x - med) for x in crabbies))

# del 2


def crabs2(inputfile):
    with open(inputfile) as f:
        crabbies = list(map(int, f.readline().split(',')))
    lomean, himean = sum(crabbies) // len(crabbies), round(sum(crabbies) / len(crabbies))
    losum, hisum = 0, 0
    for x in crabbies:
        lodist, hidist = abs(x - lomean), abs(x - himean)
        losum += lodist * (lodist + 1) / 2
        hisum += hidist * (hidist + 1) / 2
    print(min(losum, hisum))


crabs2('7-test.txt')
crabs2('7-input.txt')
