with open('2022\\3\\3-input.txt') as f:
    sacks = f.readlines()
    
alfa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

tot = 0

for s1,s2,s3 in zip(sacks[0::3],sacks[1::3],sacks[2::3]):
    for l in s1:
        if l in s2 and l in s3:
            tot += alfa.index(l) + 1
            break

print(tot)