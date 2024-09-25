# del 1:
with open('1-input.txt') as depths:
    vals = [int(x) for x in depths.read().splitlines()]

'''i, deeps = 0, 0
while i < len(vals) - 1:
    if vals[i] < vals[i + 1]:
        deeps += 1
    i += 1'''

# del 2:
i, slides = 0, []
while i < len(vals) - 2:
    slides.append(sum(vals[i:i+3]))
    i += 1

i, deeps = 0, 0
while i < len(slides) - 1:
    if slides[i] < slides[i + 1]:
        deeps += 1
    i += 1

print(deeps)
