import re
import time

def part1(f):
    total = 0
    input = f.readlines()

    for line in input:
        line = re.sub(r'.*:(.*)(?:\n|$)', r'\1', line)
        line = re.sub(r'\b(\d+)\b(?=.*\|.*\b\1\b)', r'x', line)
        line = re.sub(r'[^x]', '', line)

        if len(line) > 0:
            total += 2 ** (len(line) - 1)

    return total

def part2(f):
    input = f.readlines()
    copies = [1] * len(input)

    for i, line in enumerate(input):
        line = re.sub(r'.*:(.*)(?:\n|$)', r'\1', line)
        line = re.sub(r'\b(\d+)\b(?=.*\|.*\b\1\b)', r'x', line)
        line = re.sub(r'[^x]', '', line)

        for j in range(len(line)):
            copies[i + j + 1] += copies[i]

    return sum(copies)

with open('day4_input.txt', 'r') as f:
    print('Results from Part 1: {}'.format(part1(f)))

with open('day4_input.txt', 'r') as f:
    print('Results from Part 2: {}'.format(part2(f)))