import re
import time

def part1(f):
    total = 0
    input = f.readlines()

    nums = []
    specs = []
    for line in input:
        nums.append([m.span() for m in re.finditer(r'\d+', line.strip())])
        specs.append([m.start() for m in re.finditer(r'[^\d\.]', line.strip())])

    for i, row in enumerate(specs):
        if len(row) == 0:
            continue

        for ch in row:
            # check current row
            for span in nums[i]:
                if span[1] == ch:
                    total += eval(input[i][span[0]:span[1]])
                elif span[0] == ch + 1:
                    total += eval(input[i][span[0]:span[1]])

            if i != 0:
                for span in nums[i - 1]:
                    if ch <= span[1] <= ch + 2:
                        total += eval(input[i - 1][span[0]:span[1]])
                    elif ch - 1 <= span[0] <= ch + 1:
                        total += eval(input[i - 1][span[0]:span[1]])

            if i != len(specs):
                for span in nums[i + 1]:
                    if ch <= span[1] <= ch + 2:
                        total += eval(input[i + 1][span[0]:span[1]])
                    elif ch - 1 <= span[0] <= ch + 1:
                        total += eval(input[i + 1][span[0]:span[1]])

    return total

def part2(f):
    total = 0
    input = f.readlines()

    nums = []
    specs = []
    for line in input:
        nums.append([m.span() for m in re.finditer(r'\d+', line.strip())])
        specs.append([m.start() for m in re.finditer(r'\*', line.strip())])

    for i, row in enumerate(specs):
        if len(row) == 0:
            continue

        for ch in row:
            gears = []

            for span in nums[i]:
                if span[1] == ch:
                    gears.append(eval(input[i][span[0]:span[1]]))
                elif span[0] == ch + 1:
                    gears.append(eval(input[i][span[0]:span[1]]))

            if i != 0:
                for span in nums[i - 1]:
                    if ch <= span[1] <= ch + 2:
                        gears.append(eval(input[i - 1][span[0]:span[1]]))
                    elif ch - 1 <= span[0] <= ch + 1:
                        gears.append(eval(input[i - 1][span[0]:span[1]]))

            if i != len(specs):
                for span in nums[i + 1]:
                    if ch <= span[1] <= ch + 2:
                        gears.append(eval(input[i + 1][span[0]:span[1]]))
                    elif ch - 1 <= span[0] <= ch + 1:
                        gears.append(eval(input[i + 1][span[0]:span[1]]))
            
            if len(gears) > 1:
                t_val = 1
                for val in gears:
                    t_val *= val

                total += t_val

    return total

with open('day3_input.txt', 'r') as f:
    print('Results from Part 1: {}'.format(part1(f)))

with open('day3_input.txt', 'r') as f:
    print('Results from Part 2: {}'.format(part2(f)))