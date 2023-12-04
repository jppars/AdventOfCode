import re
import time

def part1(f):
    input = f.read()

    input = re.sub(r'\n', r'|', input)
    crate_lines = re.sub(r'(.*)\|\|.*', r'\1', input)
    crate_lines = crate_lines.split('|')
    crate_idxs = [m.start() for m in re.finditer(r'\d', crate_lines.pop())]
    crates = []
    for i, idx in enumerate(crate_idxs):
        crates.append([])
        for j, row in enumerate(crate_lines[::-1]):
            if row[idx] != ' ':
                crates[i].append(row[idx])


    moves = re.sub(r'.*(?<=\|)\|(.*)', r'\1', input)
    moves = re.sub(r'move (\d+) from (\d) to (\d)(\||$)', r'\1: crates[\3 - 1].append(crates[\2 - 1].pop())\4', moves)
    moves = moves.split('|')
    for move in moves:
        repeat = int(move.strip().split(':')[0].strip())
        command = move.strip().split(':')[1].strip()

        for i in range(repeat):
            eval(command)

    highest = ''
    for stack in crates:
        highest += stack[-1]

    return highest

def part2(f):
    input = f.read()

    input = re.sub(r'\n', r'|', input)
    crate_lines = re.sub(r'(.*)\|\|.*', r'\1', input)
    crate_lines = crate_lines.split('|')
    crate_idxs = [m.start() for m in re.finditer(r'\d', crate_lines.pop())]
    crates = []
    for i, idx in enumerate(crate_idxs):
        crates.append([])
        for j, row in enumerate(crate_lines[::-1]):
            if row[idx] != ' ':
                crates[i].append(row[idx])


    moves = re.sub(r'.*(?<=\|)\|(.*)', r'\1', input)
    moves = re.sub(r'move (\d+) from (\d) to (\d)(\||$)', r'\1: stack.append(crates[\2 - 1].pop())\ncrates[\3 - 1].append(stack.pop())\4', moves)
    moves = moves.split('|')
    for move in moves:
        repeat = int(move.strip().split(':')[0].strip())
        command = move.strip().split(':')[1].strip()
        stack = []

        for i in range(repeat):
            eval(command.split('\n')[0])
        
        for i in range(repeat):
            eval(command.split('\n')[1])

    highest = ''
    for stack in crates:
        highest += stack[-1]

    return highest

with open('day5_input.txt', 'r') as f:
    print('Results from Part 1: {}'.format(part1(f)))

with open('day5_input.txt', 'r') as f:
    print('Results from Part 2: {}'.format(part2(f)))
