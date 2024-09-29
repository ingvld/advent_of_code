with open('2-input.txt') as f:
    code = [int(x) for x in f.read().strip().split(',')]

code[1],code[2] = 12,2

code_length = len(code)
i = 0

while i < code_length:
    match code[i]:
        case 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
        case 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
        case 99:
            break
    i += 4

print(code[0])
