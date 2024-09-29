def find_match():
    seen = set()

    with open('2-input') as f:
        for line in f.readlines():
            for i in range(0,len(line)):
                letters = line[:i] + line[i+1:]
                if (letters, i) in seen:
                    print(letters)
                    return
                seen.add((letters, i))

find_match()