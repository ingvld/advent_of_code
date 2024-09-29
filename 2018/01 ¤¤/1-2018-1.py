# del 1
result_freq = 0

with open('1-input') as f:
    for line in f.readlines():
        result_freq += int(line)

print(result_freq)