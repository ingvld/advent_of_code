with open('2022\\7\\7-input.txt') as f:
    output = f.readlines()

def get_parent_dir(dir):
    if '\\' not in dir:
        return None
    return dir[:dir.rindex('\\')]

current_dir = ''
dir_weight = {}

for line in output:
    if line[0] == '$':
        if line[2:4] == 'cd':
            move = line[5:].strip()
            if move == '..':
                current_dir = get_parent_dir(current_dir)
            else:
                current_dir = current_dir + '\\' + move if current_dir else move
                dir_weight[current_dir] = 0

    elif line[0] != 'd':
        weight = int(line.split()[0])
        dir_to_add_weight = current_dir

        while dir_to_add_weight:
            dir_weight[dir_to_add_weight] += weight
            dir_to_add_weight = get_parent_dir(dir_to_add_weight)

space_needed = 30000000 - (70000000 - dir_weight['/'])
to_delete = 70000000

for weight in dir_weight.values():
    if weight >= space_needed and weight < to_delete:
        to_delete = weight

print(to_delete)