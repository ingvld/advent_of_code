def oppg1(filename):

    total = 0

    with open(filename) as f:
        for line in f.readlines():

            winners,numbers = line.split(':')[1].split('|')
            winners = set(map(int, winners.split()))
            numbers = set(map(int, numbers.split()))

            matches = winners.intersection(numbers)

            if matches:
                total += pow(2, len(matches)-1)

    print(total)


def oppg2(filename):

    with open(filename) as f:

        cards = f.readlines()
        copies = [1 for _ in range(len(cards))]

        for i in range(len(cards)):
            winners,numbers = cards[i].split(':')[1].split('|')
            winners = set(map(int, winners.split()))
            numbers = set(map(int, numbers.split()))

            number_of_matches = len(winners.intersection(numbers))

            for n in range(i+1,min(i+number_of_matches+1,len(cards))):
                copies[n] += copies[i]
    
    print(sum(copies))

oppg2('4-input.txt')