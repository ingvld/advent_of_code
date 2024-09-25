with open('2017\\1\\1-input.txt') as f:
    seq = f.read()

seqln = len(seq)
half = int(len(seq)/2)
tot = 0

for n in range(seqln):
    next = n + half if n + half < seqln else n - half

    if seq[n] == seq[next]:
            tot += int(seq[n])

print(tot)