import re
import time

lower_offset = 96
upper_offset = 65 - 27

def part1():
    total = 0
    with open('day3_input.txt', 'r') as f:
        for line in f:
            line = line.strip()

            line1 = line[:int(len(line)/2)]
            line2 = line[int(len(line)/2):]

            for ch in line1:
                if ch in line2:
                    if ord(ch) < 97:
                        total += ord(ch) - upper_offset
                    else:
                        total += ord(ch) - lower_offset
                    break

    return total

def part2():
    total = 0
    with open('day3_input.txt', 'r') as f:
        input = f.read().split('\n')
        for idx in range(0, len(input), 3):
            for ch in input[idx]:
                if ch in input[idx + 1] and ch in input[idx + 2]:
                    if ord(ch) < 97:
                        total += ord(ch) - upper_offset
                    else:
                        total += ord(ch) - lower_offset
                    break

    return total

print('Results of Part 1: {}'.format(part1()))
print('Results of Part 2: {}'.format(part2()))