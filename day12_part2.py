# Open the file called "input.txt" in the same directory as this file.
input_file = open("input2.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()

import itertools

def pprint(x):
    for r in x:
        print(r)

input = [x.split() for x in input]
springs = [] 
conditions = []

for s,c in input:
    springs.append(s)
    conditions.append(c)

springs = [x for x in springs]
conditions = [tuple(map(int,x.split(","))) for x in conditions]
#print(springs)
#print(conditions)
def determine_valid_ways(spring, cond):

    if spring == "": return 0 if len(cond) > 0 else 1

    if len(cond) == 0: return 0 if "#" in spring else 1

    count = 0

    if spring[0] in ".?":
        count += determine_valid_ways(spring[1:], cond)
    elif spring[0]  in "#?":
        if "." not in spring[:cond[0]] and (len(spring) == cond[0] or spring[cond[0]] != "#"): 
            count += determine_valid_ways(spring[cond[0] + 1:], cond[1:])
    return count

print(sum(determine_valid_ways(x,y) for x,y in zip(springs, conditions)))
   