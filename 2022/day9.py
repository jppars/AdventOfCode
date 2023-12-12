import re
import cmath

DIR_MAP = {
    'U': 1j,
    'D': -1j,
    'L': -1,
    'R': 1
}

def part1(f):
    lines = f.readlines()

    head = 0 + 0j
    tail = 0 + 0j
    tails = set()
    for line in lines:
        dir, dist = line.strip().split()
        dist = int(dist)
        dir = DIR_MAP[dir]

        for i in range(dist):
            head += dir

            if abs(head - tail) >= 2:
                tails.add(tail)
                tail = head - dir
    
    tails.add(tail)

    return len(tails)

def sign(val):
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0

def part2(f):
    lines = f.readlines()

    nodes = [0 + 0j for i in range(10)]
    tails = set()
    for line in lines:
        dir, dist = line.strip().split()
        dist = int(dist)
        dir = DIR_MAP[dir]

        for i in range(dist):
            nodes[0] += dir
            update = 0

            for j in range(len(nodes) - 1):
                if abs(nodes[j] - nodes[j + 1]) >= 2:
                    if j == len(nodes) - 2:
                        tails.add(nodes[j + 1])

                    update = sign(nodes[j].real - nodes[j + 1].real) + 1j * sign(nodes[j].imag - nodes[j + 1].imag)
                    nodes[j + 1] += update
    
    tails.add(nodes[-1])

    return len(tails)

with open('inputs/day9.txt', 'r') as f:
    print('Results from Part 1: {}'.format(part1(f)))

with open('inputs/day9.txt', 'r') as f:
    print('Results from Part 2: {}'.format(part2(f)))