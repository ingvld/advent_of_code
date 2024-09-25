import heapq
from math import lcm

def oppg1(filename):
    
    connections = {}

    with open(filename) as f:
        instructions = f.readline().strip()

        for line in f.readlines()[1:]:
            connections[line[:3]] = (line[7:10], line[12:15])
    
    current = 'AAA'
    steps = 0
    i = 0

    while current != 'ZZZ':
        if instructions[i] == 'L':
            current = connections[current][0]
        else:
            current = connections[current][1]

        steps += 1

        i += 1
        if i >= len(instructions):
            i = 0
    
    print(steps)


def oppg2(filename):
    
    connections = {}
    start_nodes = []

    with open(filename) as f:
        instructions = f.readline().strip()

        for line in f.readlines()[1:]:
            if line[2] == 'A':
                start_nodes.append(line[:3])
            connections[line[:3]] = (line[7:10], line[12:15])

    factors = []

    for start_node in start_nodes:
        steps = 0
        i = 0

        while start_node[2] != 'Z':
            if instructions[i] == 'L':
                start_node = connections[start_node][0]
            else:
                start_node = connections[start_node][1]

            steps += 1

            i += 1
            if i >= len(instructions):
                i = 0
        factors.append(steps)
    
    print(lcm(*factors))

oppg2("8-input.txt")