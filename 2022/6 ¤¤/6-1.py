with open('2022\\6\\6-input.txt') as f:
    data = f.read()


seq = ''

i = 0

while len(seq) < 4:
    letter = data[i]

    seq += letter

    if seq.count(letter) > 1:
        seq = seq[seq.index(letter)+1:]

    i += 1

print(i)
