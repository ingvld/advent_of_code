twos, threes = 0, 0

with open('2-input') as f:
    for line in f.readlines():
        letter_counts = {}
        
        for letter in line:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        
        two, three = False, False
        for n in letter_counts.values():
            if n == 2:
                two = True
            elif n == 3:
                three = True
        if two:
            twos += 1
        if three:
            threes += 1

print(twos*threes)