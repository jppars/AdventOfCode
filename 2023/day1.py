import re
import time
# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you 
# ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say 
# the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you 
# into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input)
# has been amended by a very young Elf who was apparently just excited to show off her art skills.
# Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally
# contained a specific calibration value that the Elves now need to recover. On each line,
# the calibration value can be found by combining the first digit and the last digit 
# (in that order) to form a single two-digit number.

def part1():
    sum = 0
    with open('day1_input.txt', 'r') as f:
        for line in f:
            line = re.sub(r'^[^0-9]*([0-9]).*([0-9])[^0-9]*$', r'\1\2', line)
            line = re.sub(r'^[^0-9]*([0-9])[^0-9]*$', r'\1\1', line)

            sum += eval(line)
    return sum

def part2():
    sum = 0
    with open('day1_input.txt', 'r') as f:
        input = f.read()

    input = input + 'Dictionary:one=1:two=2:three=3:four=4:five=5:six=6:seven=7:eight=8:nine=9'
    input = re.sub(r'\n', ' ', input)
    input = re.sub(r'(?<=\b)[^0-9 ]*?(one|two|three|four|five|six|seven|eight|nine)(?=.*:\1=(.))', r'\2', input)
    input = re.sub(r'[^0-9 ]*(one|two|three|four|five|six|seven|eight|nine)[^0-9 ]*(?=\b.*:\1=(.))', r'\2', input)

    for i, line in enumerate(input.split(' ')):
        if i == len(input.split(' ')) - 1:
            break
        
        line = re.sub(r'^[^0-9]*([0-9]).*([0-9])[^0-9]*$', r'\1\2', line)
        line = re.sub(r'^[^0-9]*([0-9])[^0-9]*$', r'\1\1', line)

        sum += eval(line)


    return sum

print('Results from Part 1: {}'.format(part1()))
print('Results from Part 2: {}'.format(part2()))
time.sleep(1)

    