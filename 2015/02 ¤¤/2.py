def wrapping1(filnavn):
    with open(filnavn) as f:
        boxes = [list(map(int, box[:-1].split('x'))) for box in f.readlines()]
    total_paper = 0
    for box in boxes:
        l, w, h = box[0], box[1], box[2]
        sides = [l*w, w*h, h*l]
        total_paper += 2*sum(sides) + min(sides)
    print(total_paper)


def wrapping2(filnavn):
    with open(filnavn) as f:
        boxes = [list(map(int, box[:-1].split('x'))) for box in f.readlines()]
    total_ribbon = 0
    for box in boxes:
        l, w, h = box[0], box[1], box[2]
        shortsides = sorted([l, w, h])[:-1]
        total_ribbon += sum(shortsides)*2 + l*w*h
    print(total_ribbon)


wrapping2('2/2-input.txt')
