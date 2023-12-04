import re
import time

def part1():
    total = 0
    with open('day4_input.txt', 'r') as f:
        input = f.read()

    input = re.sub(r'(\d+)-(\d+),(\d+)-(\d+)', r'([\1,\3],[\2,\4])', input)

    pairs = input.split('\n')

    for pair in pairs:
        starts = eval(pair)[0]
        ends = eval(pair)[1]

        if starts[0] <= starts[1] and ends[0] >= ends[1]:
            total += 1
        elif starts[0] >= starts[1] and ends[0] <= ends[1]:
            total += 1

    return total

def part2():
    total = 0
    with open('day4_input.txt', 'r') as f:
        input = f.read()

    input = re.sub(r'(\d+)-(\d+),(\d+)-(\d+)', r'([\1,\3],[\2,\4])', input)

    pairs = input.split('\n')

    for pair in pairs:
        starts = eval(pair)[0]
        ends = eval(pair)[1]

        if starts[0] <= starts[1] and starts[1] <= ends[0]:
            total += 1
        elif starts[1] <= starts[0] and starts[0] <= ends[1]:
            total += 1

    return total

print('Result of Part 1: {}'.format(part1()))
print('Result of Part 2: {}'.format(part2()))