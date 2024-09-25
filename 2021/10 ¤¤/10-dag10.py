# del 1

def errors1(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    score, scores = 0, {')': 3, ']': 57, '}': 1197, '>': 25137}
    for line in lines:
        corrupt, i, temp = 0, 0, []
        pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
        while not corrupt and i < len(line):
            x = line[i]
            if x in pairs:
                temp.append(x)
            else:
                if not temp or pairs[temp[-1]] != x:
                    corrupt = 1
                    score += scores[x]
                else:
                    temp.pop()
            i += 1
    print(score)


# del 2

def errors2(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    scores, values = [], {')': 1, ']': 2, '}': 3, '>': 4}
    for line in lines:
        corrupt, i, temp = 0, 0, []
        pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
        while not corrupt and i < len(line):
            x = line[i]
            if x in pairs:
                temp.append(x)
            else:
                if not temp or pairs[temp[-1]] != x:
                    corrupt = 1
                else:
                    temp.pop()
            i += 1
        if temp and not corrupt:
            score = 0
            for x in temp[::-1]:
                score *= 5
                score += values[pairs[x]]
            scores.append(score)
    print(sorted(scores)[len(scores)//2])


errors2('10-input.txt')
