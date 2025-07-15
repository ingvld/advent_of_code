def polymer1(filename):
    with open(filename) as f:
        polymer = f.readline()[:-1]
        rules = {}
        for line in f.readlines()[1:]:
            x, y = line[:-1].split(' -> ')
            rules[x] = y

    step = 0
    while step < 10:
        inserts = []
        i = 0
        while i < len(polymer)-1:
            combo = polymer[i:i+2]
            if combo in rules:
                inserts.append((i+1, rules[combo]))
            i += 1
        for x in inserts[::-1]:
            n, y = x[0], x[1]
            polymer = polymer[:n] + y + polymer[n:]
        step += 1

    letcount = {}
    for x in polymer:
        if x in letcount:
            letcount[x] += 1
        else:
            letcount[x] = 1

    print(max(letcount.values()) - min(letcount.values()))


def polymer2(filename):
    with open(filename) as f:
        fline = f.readline()[:-1]
        rules, combocount_template = {}, {}
        for line in f.readlines()[1:]:
            x, y = line[:-1].split(' -> ')
            rules[x] = (y, (x[0]+y, y+x[1]))
            combocount_template[x] = 0
        combocount = combocount_template.copy()
        for i in range(len(fline)-1):
            combo = fline[i:i+2]
            if combo in combocount:
                combocount[combo] += 1
        letcount = {x[0]: 0 for x in rules.values()}
        for x in fline:
            letcount[x] += 1

    step = 0
    while step < 40:
        new_combocount = combocount_template.copy()
        for combo in combocount:
            n = combocount[combo]
            new_element, new_combos = rules[combo][0], rules[combo][1]
            letcount[new_element] += n
            for new_combo in new_combos:
                if new_combo in rules:
                    new_combocount[new_combo] += n
        combocount = new_combocount.copy()
        step += 1
    letcountvals = letcount.values()
    print(max(letcountvals) - min(letcountvals))


polymer2('14-input.txt')
