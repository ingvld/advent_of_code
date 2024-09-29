with open('2-input.txt') as f:
    code = [int(x) for x in f.read().strip().split(',')]

code_length = len(code)

def run_code(noun,verb):
    c_code = code[:]

    c_code[1],c_code[2] = noun,verb

    i = 0

    while i < code_length:
        match c_code[i]:
            case 1:
                c_code[c_code[i+3]] = c_code[c_code[i+1]] + c_code[c_code[i+2]]
            case 2:
                c_code[c_code[i+3]] = c_code[c_code[i+1]] * c_code[c_code[i+2]]
            case 99:
                break
        i += 4

    return(c_code[0])

for i in range(100):
    for n in range(100):
        if run_code(i,n) == 19690720:
            print(100*i+n)
            break