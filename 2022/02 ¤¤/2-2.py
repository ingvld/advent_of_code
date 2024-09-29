with open('2022\\2\\2-input.txt') as f:
    matches = [[x[0], x[2]] for x in f.readlines()]

def get_score(op, oc):
    vals = {'X':0, 'Y':3, 'Z':6}
    beats = {'A':{'X':3,'Y':1,'Z':2},'B':{'X':1,'Y':2,'Z':3},'C':{'X':2,'Y':3,'Z':1}}

    score = vals[oc] + beats[op][oc]

    return score

tot_score = 0

for match in matches:
    tot_score += get_score(match[0],match[1])

print(tot_score)
