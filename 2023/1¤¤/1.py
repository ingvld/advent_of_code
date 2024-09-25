def calibrate1(input_file):
    with open(input_file) as f:

        result = 0

        for line in f.readlines():
            first, last = None, None
            for x in line:
                if x in '0123456789':
                    if first == None:
                        first = x
                    last = x
            result += int(first+last)
    print(result)


def calibrate2(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    result = 0

    for line in lines:
        first, last = None, None
        lver = ''
        
        for x in line:
            if x in '123456789':
                if first == None:
                    first = x
                last = x
            elif x in 'efghinorstuvwxz':
                lver += x
                if len(lver) >= 3 and lver[-3:] in {'one','two','six'}:
                    num = {'one':'1','two':'2','six':'6'}[lver[-3:]]
                    if first == None:
                        first = num
                    last = num
                elif len(lver) >= 4 and lver[-4:] in {'four','five','nine'}:
                    num = {'four':'4','five':'5','nine':'9'}[lver[-4:]]
                    if first == None:
                        first = num
                    last = num
                elif len(lver) >= 5 and lver[-5:] in {'three','seven','eight'}:
                    num = {'three':'3','seven':'7','eight':'8'}[lver[-5:]]
                    if first == None:
                        first = num
                    last = num
            else:
                lver = ''
        result += int(first+last)
    
    print(result)

calibrate2('1-input')

        

