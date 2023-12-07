# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()

from collections import Counter
from functools import cmp_to_key

input = [x.split() for x in input]
input = [(list(x), int(y)) for [x,y] in input]

def convert(x):
    match x:
        case 'T': return 10
        case 'J': return 11
        case 'Q': return 12
        case 'K': return 13
        case 'A': return 14

    return int(x)

for i in range(len(input)):
    hand,bid = input[i]
    input[i] = (list(hand),bid)


def compare(line1, line2):
    a = line1[0]
    b = line2[0]
    if a == b: return 0
    a = Counter(a)
    b = Counter(b)

    # Compare hand strength by looking at number of unique characters.
    if len(a.keys()) > len(b.keys()):
        return -1
    elif len(a.keys()) < len(b.keys()):
        return 1
    else:
        # For ties in number of unique characters, (4 of a kind, full house), look at number of most frequent characters.
        for (ai, a_count),(bi, b_count) in zip(a.most_common(), b.most_common()):
            if a_count > b_count:
                return 1
            elif a_count < b_count:
                return -1

    # Getting to this part of the code means a tie in hand strength, go through each character and compare individual card strength.
    a,b = list(map(convert,line1[0])), list(map(convert,line2[0]))
    for ai,bi in zip(a,b):
        if ai < bi:
            return -1
        elif ai > bi:
            return 1
    
    return 0

input = sorted(input, key=cmp_to_key(compare))
ans = 0

for i,(_,bid) in enumerate(input):
    print(_)
    ans += (i+1)*bid

print(ans)