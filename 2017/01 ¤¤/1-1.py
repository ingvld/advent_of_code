with open('2017\\1\\1-input.txt') as f:
    seq = f.read()

seqln = len(seq)
tot = 0

for n in range(seqln):
    if n < seqln-1:
        if seq[n] == seq[n+1]:
            tot += int(seq[n])
    else:
        if seq[n] == seq[0]:
            tot += int(seq[n])

print(tot)