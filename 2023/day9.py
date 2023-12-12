import re
import time

def diff(vals):
    new_vals = [0] * (len(vals) - 1)
    for i in range(len(vals) - 1):
        new_vals[i] = vals[i + 1] - vals[i]

    return new_vals

def part1(f):
    test_input = f.readlines()

    total = 0
    for line in test_input:
        nums = [int(val) for val in re.findall('[^ ]+', line)]

        diffs = [nums]
        while True:
            diffs.append(diff(diffs[-1]))

            zeroed = True
            for i in diffs[-1]:
                if i != 0:
                    zeroed = False
                    break
            if zeroed:
                break

        diffs[-1].append(0)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i + 1][-1] + diffs[i][-1])

        total += diffs[0][-1]

    return total

def part2(f):
    test_input = f.readlines()

    total = 0
    for line in test_input:
        nums = [int(val) for val in re.findall('[^ ]+', line)]

        diffs = [nums]
        while True:
            diffs.append(diff(diffs[-1]))

            zeroed = True
            for i in diffs[-1]:
                if i != 0:
                    zeroed = False
                    break
            if zeroed:
                break

        diffs[-1].insert(0, 0)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].insert(0, diffs[i][0] - diffs[i + 1][0])

        total += diffs[0][0]

    return total

with open('day9_input.txt', 'r') as f:
    print('Results from Part 1: {}'.format(part1(f)))

with open('day9_input.txt', 'r') as f:
    print('Results from Part 2: {}'.format(part2(f)))
