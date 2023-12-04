import re
import time

def part1(f):
    input = f.read().strip()

    match = re.search(r'(.)(?!\1)(.)(?!\1|\2)(.)(?!\1|\2|\3).', input)

    return match.end()

def part2(f):
    input = f.read()

    characters = 14
    match_string = r''
    for i in range(characters - 1):
        match_string += r'(.)(?!'
        for j in range(i + 1):
            if j == i:
                match_string += r'\{})'.format(j + 1)
            else:
                match_string += r'\{}|'.format(j + 1)
    match_string += r'.'

    match = re.search(match_string, input)
    return match.end()

with open('day6_input.txt', 'r') as f:
    print('Results from Part 1: {}'.format(part1(f)))

with open('day6_input.txt', 'r') as f:
    print('Results from Part 2: {}'.format(part2(f)))