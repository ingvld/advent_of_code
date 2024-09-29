def lights1(filnavn):
    with open(filnavn) as f:
        input_lines = f.readlines()
        instructions = []
        for line in input_lines:
            for x in ['turn on', 'toggle', 'turn off']:
                if x in line:
                    action = x
                    line = line[len(action):]
                    break
            positions = [list(map(int, x.split(','))) for x in line[1:-1].split(' through ')]
            instructions.append([action, positions])

    ons, states = 0, [[0 for n in range(0, 1001)] for i in range(0, 1000)]
    for action, lights in instructions:
        for x in range(lights[0][0], lights[1][0]+1):
            low = lights[0][1] if lights[0][1] < lights[1][1] else lights[1][1]
            high = lights[0][1] if lights[0][1] != low else lights[1][1]
            for i in range(low, high+1):
                if action == 'turn on' or (action == 'toggle' and states[x][i] == 0):
                    if states[x][i] == 0:
                        states[x][i] = 1
                        ons += 1
                else:
                    if states[x][i] == 1:
                        states[x][i] = 0
                        ons -= 1
    print(ons)


def lights2(filnavn):
    with open(filnavn) as f:
        input_lines = f.readlines()
        instructions = []
        for line in input_lines:
            for x in ['turn on', 'toggle', 'turn off']:
                if x in line:
                    action = x
                    line = line[len(action):]
                    break
            positions = [list(map(int, x.split(','))) for x in line[1:-1].split(' through ')]
            instructions.append([action, positions])

    ons, states = 0, [[0 for n in range(0, 1001)] for i in range(0, 1000)]
    for action, lights in instructions:
        for x in range(lights[0][0], lights[1][0]+1):
            low = lights[0][1] if lights[0][1] < lights[1][1] else lights[1][1]
            high = lights[0][1] if lights[0][1] != low else lights[1][1]
            for i in range(low, high+1):
                if action == 'turn on':
                    states[x][i] += 1
                    ons += 1
                elif action == 'toggle':
                    states[x][i] += 2
                    ons += 2
                else:
                    if states[x][i] > 0:
                        states[x][i] -= 1
                        ons -= 1
    print(ons)


lights2('6/6-input.txt')
