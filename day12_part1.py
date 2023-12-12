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

springs = [list(x) for x in springs]
conditions = [x.split(",") for x in conditions]
for i in range(len(conditions)):
    conditions[i] = [int(x) for x in conditions[i]]
    

def determine_valid_ways(spring, condition):

    temp = spring.copy()
    unknown_locations = [i for i,x in enumerate(spring) if x == "?"]
    unknown_count = len(unknown_locations)
    possible_configs = itertools.product([0,1], repeat=unknown_count)
    ways = 0

    for config in possible_configs:
        #assert(len(config) == len(unknown_locations))

        for i,val in zip(unknown_locations,config):
            temp[i] = "." if val else "#"

        # determine validity
        if [len(x) for x in "".join(temp).split(".") if x != ""] == condition: ways += 1
    return ways


print(sum(determine_valid_ways(x,y) for x,y in zip(springs,conditions)))
"""
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#
"""