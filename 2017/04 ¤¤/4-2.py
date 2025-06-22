import sys

def validate_passphrase(pp):
    combos = set()
    for word in pp.split():
        combo = ''.join(sorted(word))
        if combo in combos:
            return 0
        combos.add(combo)
    return 1

with open(sys.argv[1]) as f:
    tot = 0
    for line in f.readlines():
        tot += validate_passphrase(line)

print(tot)
