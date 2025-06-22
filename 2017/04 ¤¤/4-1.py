print(sum([1 if len(line.strip().split()) == len(set(line.strip().split())) else 0 for line in open('2017/4/4-input.txt').readlines()]))
