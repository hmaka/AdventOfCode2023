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
        case 'Q': return 12
        case 'K': return 13
        case 'A': return 14
        case 'J': return 1

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

    if 'J' in a:
        j_count = a['J']
        del a['J']
        if len(a) == 0: a['A'] = 5
        else:  a[a.most_common(1)[0][0]] += j_count 

    if 'J' in b:
        j_count = b['J']
        del b['J']
        if len(b) == 0: b['A'] = 5
        else:  b[b.most_common(1)[0][0]] += j_count 
 
    if len(a.keys()) > len(b.keys()):
        return -1
    elif len(a.keys()) < len(b.keys()):
        return 1
    else:
        for (ai, a_count),(bi, b_count) in zip(a.most_common(), b.most_common()):
            if a_count > b_count:
                return 1
            elif a_count < b_count:
                return -1
                
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
    ans += (i+1)*bid

print(ans)