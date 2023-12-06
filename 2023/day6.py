import re
import time

def part1(f):
    input = f.readlines()
    times = re.findall(r'\b\d+\b', input[0])
    dist = re.findall(r'\b\d+\b', input[1])
    total = 1

    for t, d in zip(times, dist):
        count = 0
        for i in range(int(t)):
            race_dist = i * (int(t) - i)
            if race_dist > int(d):
                count += 1
        total *= count

    return total

def part2(f):
    input = f.readlines()
    times = re.findall(r'\b\d+\b', input[0])
    t = ''
    for val in times:
        t += val

    dist = re.findall(r'\b\d+\b', input[1])
    d = ''
    for val in dist:
        d += val

    total = 1

    for i in range(int(t)):
        race_dist = i * (int(t) - i)
        if race_dist > int(d):
            min_win = i
            break

    for i in range(int(t), -1, -1):
        race_dist = i * (int(t) - i)
        if race_dist > int(d):
            max_win = i
            break

    return max_win - min_win + 1

with open('day6_input.txt', 'r') as f:
    print('Result from Part 1: {}'.format(part1(f)))

with open('day6_input.txt', 'r') as f:
    print('Result from Part 2: {}'.format(part2(f)))