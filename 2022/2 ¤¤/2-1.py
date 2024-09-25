with open('2022\\2\\2-input.txt') as f:
    matches = [[x[0], x[2]] for x in f.readlines()]

def get_score(op, pl):
    vals = {'X':1, 'Y':2, 'Z':3}
    beats = {'A':'Z', 'B':'X', 'C':'Y', 'X':'C', 'Y':'A', 'Z':'B'}

    score = vals[pl]

    if op == beats[pl]:
        score += 6
    elif pl != beats[op]:
        score += 3

    return score

tot_score = 0

for match in matches:
    tot_score += get_score(match[0],match[1])

print(tot_score)


