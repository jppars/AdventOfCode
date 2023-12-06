import re
import time

def part1(f):
    input = f.read()
    seeds = re.match(r'seeds:(.*?)(?=\n\n)', input).group(1)
    seeds = re.findall(r'\b\d+\b', seeds)

    maps = re.findall(r'map:\n((?:.*\n)*?)(?=\n)', input)
    for i, test_map in enumerate(maps):
        maps[i] = re.sub(r'(\d+)\s(\d+)\s(\d+)\n', r"{'source': (\2, \2 + \3), 'destination': (\1, \1 + \3)},", test_map)
        maps[i] = eval('[' + maps[i].strip()[:-1] + ']')

    min_location = 1e12

    for seed in seeds:
        current_val = int(seed)
        for i, test_map in enumerate(maps):
            for entry in test_map:
                if entry['source'][0] <= current_val < entry['source'][1]:
                    current_val = entry['destination'][0] + (current_val - entry['source'][0])
                    break
        
        if current_val < min_location:
            min_location = current_val


    return min_location

def part2(f):
    input = f.read()
    seeds = re.match(r'seeds:(.*?)(?=\n\n)', input).group(1)
    seeds = re.findall(r'\b\d+\b', seeds)
    seeds = [int(val) for val in seeds]

    maps = re.findall(r'map:\n((?:.*\n)*?)(?=\n)', input)
    for i, test_map in enumerate(maps):
        maps[i] = re.sub(r'(\d+)\s(\d+)\s(\d+)\n', r"[[\2, \2 + \3], [\1, \1 + \3]],", test_map)
        maps[i] = eval('[' + maps[i].strip()[:-1] + ']')

    valid_ranges = []
    for i, seed in enumerate(seeds):
        if i % 2 == 1:
            continue
        seed_range = (seed, seed + seeds[i + 1])
        valid_ranges.append(seed_range)

    # for j, test_map in enumerate(maps):
    #     valid_ranges.append([])
    #     for src_pair in valid_ranges[j]:
    #         test_pair = [src_pair]
    #         while len(test_pair) > 0:
    #             pair = test_pair.pop(0)
    #             for entry in test_map:
    #                 matched = True
    #                 if entry[0][0] <= pair[0] and pair[1] <= entry[0][1]:
    #                     valid_ranges[j + 1].append((entry[1][0] + (pair[0] - entry[0][0]), entry[1][1] - (entry[0][1] - pair[1])))
    #                     break

    #                 elif entry[0][0] >= pair[0] and pair[1] >= entry[0][1]:
    #                     valid_ranges[j + 1].append((entry[1][0], entry[1][1]))
    #                     test_pair.append((pair[0], entry[0][0]))
    #                     test_pair.append((entry[0][1], pair[1]))
    #                     break

    #                 elif entry[0][0] >= pair[0] and pair[1] > entry[0][0]:
    #                     valid_ranges[j + 1].append((entry[1][0], entry[1][0] + (pair[1] - entry[0][0]) + 1))
    #                     test_pair.append((pair[0], entry[0][0]))
    #                     break

    #                 elif entry[0][1] > pair[0] and pair[1] >= entry[0][1]:
    #                     valid_ranges[j + 1].append((entry[1][1] - (entry[0][1] - pair[0]) - 1, entry[1][1]))
    #                     test_pair.append((entry[0][1], pair[1]))
    #                     break
                    
    #                 else:
    #                     matched = False

    #             if not matched:
    #                 valid_ranges[j + 1].append(pair)

    min_location = 1e12
    for pair in valid_ranges[-1]:
        if pair[0] < min_location:
            min_location = pair[0]

    return min_location

with open('day5_input.txt', 'r') as f:
    print('Results of Part 1: {}'.format(part1(f)))

with open('day5_input.txt', 'r') as f:
    print('Results of Part 2: {}'.format(part2(f)))
