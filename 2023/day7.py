import re
import time

card_rank = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

def hand_rank(val, _joker):
    unique_cards = list(set(val))
    joker = 'J' in unique_cards and _joker

    if len(unique_cards) == 1 or (len(unique_cards) == 2 and joker):
        return 7
    elif len(unique_cards) == 2 or (len(unique_cards) == 3 and joker):
        max_count = 0
        for card in unique_cards:
            if card == 'J' and _joker:
                continue
            count = 0
            for cmp_card in val:
                if cmp_card == card or (cmp_card == 'J' and _joker):
                    count += 1
            if count > max_count:
                max_count = count

        if max_count == 3:
            return 5
        elif max_count == 4:
            return 6
    elif len(unique_cards) == 3 or (len(unique_cards) == 4 and joker):
        max_count = 0
        for card in unique_cards:
            if card == 'J' and _joker:
                continue
            count = 0
            for cmp_card in val:
                if card == cmp_card or (cmp_card == 'J' and _joker):
                    count += 1
            if count > max_count:
                max_count = count

        if max_count == 2:
            return 3
        else:
            return 4
    elif len(unique_cards) == 4 or (len(unique_cards) == 5 and joker):
        return 2
    else:
        return 1

def card_val(val):
    if val.isdigit():
        return int(val)
    else:
        return card_rank[val]

def part1(f):
    test_input = f.readlines()

    card_rank['J'] = 11

    games = []
    for line in test_input:
        matches = re.search(r'^(.*?)\s(.*?)$', line)
        games.append((matches.group(1), int(matches.group(2))))

    games.sort(key=lambda x: (hand_rank(x[0], False), card_val(x[0][0]), card_val(x[0][1]), card_val(x[0][2]),
                              card_val(x[0][3]), card_val(x[0][4])))

    total = 0
    for i, hand in enumerate(games):
        total += (i + 1) * hand[1]

    return total

def part2(f):
    test_input = f.readlines()

    card_rank['J'] = 1

    games = []
    for line in test_input:
        matches = re.search(r'^(.*?)\s(.*?)$', line)
        games.append((matches.group(1), int(matches.group(2))))

    games.sort(key=lambda x: (hand_rank(x[0], True), card_val(x[0][0]), card_val(x[0][1]), card_val(x[0][2]),
                              card_val(x[0][3]), card_val(x[0][4])))

    total = 0
    for i, hand in enumerate(games):
        total += (i + 1) * hand[1]

    return total

with open('day7_input.txt', 'r') as f:
    print('Results from Part 1: {}'.format(part1(f)))

with open('day7_input.txt', 'r') as f:
    print('Results from Part 2: {}'.format(part2(f)))
