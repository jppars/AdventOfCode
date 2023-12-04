import re
import time

moves = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

results = {
    'rock rock': 3,
    'rock paper': 6,
    'rock scissors': 0,
    'paper rock': 0,
    'paper paper': 3,
    'paper scissors': 6,
    'scissors rock': 6,
    'scissors paper': 0,
    'scissors scissors': 3
}

points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

def part1():
    with open('day2_input.txt', 'r') as f:
        input = f.read()

    input = re.sub('\n', '|', input)
    input += '|Dictionary:A X=4:A Y=8:A Z=3:B X=1:B Y=5:B Z=9:C X=7:C Y=2:C Z=6:'

    input = re.sub(r'((?:A|B|C) (?:X|Y|Z))(?=.*:\1=(.))', r'\2', input)
    input = re.sub(r'\|(?!.*\|).*?$', '', input)

    sum_list = [eval(val) for val in input.split('|')]

    return sum(sum_list)

def part2():
    with open('day2_input.txt', 'r') as f:
        input = f.read()

    input = re.sub('\n', '|', input)
    input += '|Dictionary:A A=4:A B=8:A C=3:B A=1:B B=5:B C=9:C A=7:C B=2:C C=6'
    input += '|Dictionary:A<B:B<C:C<A'

    input = re.sub(r'(A|B|C) Y', r'\1 \1', input)
    input = re.sub(r'(A|B|C) X(?=.*:(.)<\1)', r'\1 \2', input)
    input = re.sub(r'(A|B|C) Z(?=.*:\1<(.))', r'\1 \2', input)

    input = re.sub(r'((?:A|B|C) (?:A|B|C))(?=.*:\1=(.))', r'\2', input)
    input = re.sub(r'\|Dictionary.*?$', '', input)

    sum_list = [eval(val) for val in input.split('|')]

    return sum(sum_list)

print('Result of Part 1: {}'.format(part1()))
print('Result of Part 2: {}'.format(part2()))