with open('2017\\2\\2-input.txt') as f:
    rows = [sorted(map(int,x.split()),reverse=True) for x in f.readlines()]

tot = 0

for row in rows:
    i = 0

    while i < len(row)-1:
        n = row[i]
        for num in row[i+1:]:
            if not n % num:
                tot += n/num
                break
        i+=1

print(tot)
