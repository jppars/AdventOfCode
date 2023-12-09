import re
import time

def calc_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def calc_lcm(x, y):
    lcm = (x * y) // calc_gcd(x, y)
    return lcm

def part1(f):
    test_input = f.read()

    turns = test_input.split('\n\n')
    map = turns[1]
    turns = turns[0]

    turns = re.sub('R', '1, ', turns)
    turns = re.sub('L', '0, ', turns)
    turns = eval('[' + turns[:-1] + ']')

    matches = re.findall('(.*?) = (.*)(?=\n)', map)

    map_dict = {}
    for match in matches:
        options = match[1]
        options = re.sub(r'([A-Z]+)', r'"\1"', options)
        map_dict[match[0]] = eval(options)

    steps = 0
    pos = 'AAA'
    while pos != 'ZZZ':
        pos = map_dict[pos][turns[steps % len(turns)]]
        steps += 1

    return steps

def part2(f):
    test_input = f.read()

    turns = test_input.split('\n\n')
    map = turns[1]
    turns = turns[0]

    turns = re.sub('R', '1, ', turns)
    turns = re.sub('L', '0, ', turns)
    turns = eval('[' + turns[:-1] + ']')

    matches = re.findall('(.*?) = (.*)(?=\n)', map)

    map_dict = {}
    positions = []
    for match in matches:
        options = match[1]
        options = re.sub(r'([A-Z]+)', r'"\1"', options)
        map_dict[match[0]] = eval(options)
        if match[0][-1] == 'A':
            positions.append(match[0])

    cycles = [0] * len(positions)
    steps = 0
    while True:
        for i in range(len(positions)):
            positions[i] = map_dict[positions[i]][turns[steps % len(turns)]]
            if positions[i][-1] == 'Z' and cycles[i] == 0:
                cycles[i] = steps + 1
            elif positions[i][-1] == 'Z':
                print((steps + 1) / cycles[i] == int((steps + 1) / cycles[i]))
        steps += 1

        if 0 not in cycles:
            break

    while len(cycles) > 1:
        cycles.append(calc_lcm(cycles.pop(0), cycles.pop(0)))

    return cycles[0]

with open('day8_input.txt', 'r') as f:
    print('Results from Part 1: {}'.format(part1(f)))

with open('day8_input.txt', 'r') as f:
    print('Results from Part 2: {}'.format(part2(f)))
