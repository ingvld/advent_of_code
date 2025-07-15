# del 2
with open('1-input') as f:
    changes = list(map(int,f.readlines()))

result_freq = 0
prev_freqs = {0}
number_of_prev_freqs = 1

match, i = None, 0
while match is None:
    if i >= len(changes):
        i = 0
    result_freq += changes[i]
    prev_freqs.add(result_freq)
    if len(prev_freqs) == number_of_prev_freqs:
        match = result_freq
    number_of_prev_freqs += 1
    i += 1

print(result_freq)