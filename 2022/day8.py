import re
import time

def part1(f):
    lines = f.readlines()

    idxs = []
    for line in lines:
        line = [int(c) for c in line.strip()]
        max_height = -1
        l_idx = set()
        r_idx = set()

        for i in range(len(line)):
            if line[i] > max_height:
                max_height = line[i]
                l_idx.add(i)
        
        max_height = -1

        for i in range(len(line) - 1, -1, -1):
            if line[i] > max_height:
                max_height = line[i]
                r_idx.add(i)
        
        idxs.append(l_idx | r_idx)

    for i in range(len(lines[0].strip())):
        if i == 0 or i == len(lines[0].strip()) - 1:
            continue

        line = []
        for j in range(len(lines)):
            line.append(int(lines[j][i]))

        max_height = -1
        for j in range(len(lines)):
            if line[j] > max_height:
                max_height = line[j]
                idxs[j].add(i)

        max_height = -1
        for j in range(len(lines) - 1, -1, -1):
            if line[j] > max_height:
                max_height = line[j]
                idxs[j].add(i)
    
    visible = 0
    for row in idxs:
        for item in row:
            visible += 1

    return visible

def part2(f):
    lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = [int(c) for c in line.strip()]

    max_total = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            total = 1
            height = lines[i][j]

            for dir in [1, -1, 1j, -1j]:
                count = 0
                if dir == 1:
                    for k in range(j + 1, len(lines[i])):
                        count += 1
                        if lines[i][k] >= height:
                            break
                    total *= count
                elif dir == -1:
                    for k in range(j - 1, -1, -1):
                        count += 1
                        if lines[i][k] >= height:
                            break
                    total *= count
                if dir == 1j:
                    for k in range(i + 1, len(lines)):
                        count += 1
                        if lines[k][j] >= height:
                            break
                    total *= count
                elif dir == -1j:
                    for k in range(i - 1, -1, -1):
                        count += 1
                        if lines[k][j] >= height:
                            break
                    total *= count
            if total > max_total:
                max_total = total

    return max_total

with open('inputs/day8_input.txt', 'r') as f:
    print('Results from Part 1: {}'.format(part1(f)))

with open('inputs/day8_input.txt', 'r') as f:
    print('Results from Part 2: {}'.format(part2(f)))