import re
import time

def part1(f):
    total = 0
    input = f.readlines()

    for line in input:
        matches = re.findall(r'(?<=\s)(\d+)(?=\s.*\|.*\b\1\b)', line)

        # line = re.sub(r'.*:(.*)(?:\n|$)', r'\1', line)
        # line = re.sub(r'\b(\d+)\b(?=.*\|.*\b\1\b)', r'x', line)
        # line = re.sub(r'[^x]', '', line)

        if len(matches) > 0:
            total += 2 ** (len(matches) - 1)

    return total

def part2(f):
    input = f.readlines()
    copies = [1] * len(input)

    for i, line in enumerate(input):
        matches = re.findall(r'(?<=\s)(\d+)(?=\s.*\|.*\b\1\b)', line)

        # line = re.sub(r'.*:(.*)(?:\n|$)', r'\1', line)
        # line = re.sub(r'\b(\d+)\b(?=.*\|.*\b\1\b)', r'x', line)
        # line = re.sub(r'[^x]', '', line)

        for j in range(len(matches)):
            copies[i + j + 1] += copies[i]

    return sum(copies)

with open('day4_input.txt', 'r') as f:
    print('Results from Part 1: {}'.format(part1(f)))

with open('day4_input.txt', 'r') as f:
    print('Results from Part 2: {}'.format(part2(f)))