# del1
def seven_segment1(filename):
    with open(filename) as f:
        segments = [y for x in f.readlines() for y in x.split()[-4:]]
    res = 0
    for x in segments:
        if len(x) in [2, 3, 4, 7]:
            res += 1
    print(res)


def seven_segment2(filename):
    with open(filename) as f:
        entries = [x.split() for x in f.readlines()]
    total = 0
    for entry in entries:
        digs, lets = {}, {}
        for x in entry[:10]:
            if len(x) == 2:
                digs[1] = sorted(x)
            elif len(x) == 3:
                digs[7] = sorted(x)
            elif len(x) == 4:
                digs[4] = sorted(x)
            elif len(x) == 7:
                digs[8] = sorted(x)

        for letter in 'abcdefg':
            letcount = ''.join(entry[:10]).count(letter)
            if letcount == 9:
                lets['bottomright'] = letter
            elif letcount == 8:
                if letter in digs[4]:
                    lets['topright'] = letter
                else:
                    lets['top'] = letter
            elif letcount == 7:
                if letter in digs[4]:
                    lets['mid'] = letter
                else:
                    lets['bottom'] = letter
            elif letcount == 6:
                lets['topleft'] = letter
            else:
                lets['bottomleft'] = letter

        digs[0] = sorted(''.join([lets['top'], lets['topright'],
                                 lets['topleft'], lets['bottomleft'], lets['bottomright'], lets['bottom']]))
        digs[2] = sorted(''.join([lets['top'], lets['topright'],
                                  lets['mid'], lets['bottomleft'], lets['bottom']]))
        digs[3] = sorted(''.join([lets['top'], lets['topright'],
                                 lets['mid'], lets['bottomright'], lets['bottom']]))
        digs[5] = sorted(''.join([lets['top'], lets['topleft'],
                                 lets['mid'], lets['bottomright'], lets['bottom']]))
        digs[6] = sorted(''.join([lets['top'], lets['topleft'],
                                 lets['mid'], lets['bottomleft'], lets['bottomright'], lets['bottom']]))
        digs[9] = sorted(''.join([lets['top'], lets['topright'],
                                 lets['topleft'], lets['mid'], lets['bottomright'], lets['bottom']]))

        num = ''
        for x in entry[-4:]:
            sx = sorted(x)
            for y in digs:
                if sx == digs[y]:
                    num += str(y)
        total += int(num)
    print(total)


seven_segment2('8-input.txt')


lol = 'hei'
print(lol[1:3])
