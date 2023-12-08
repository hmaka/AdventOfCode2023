# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()

instructions = [0 if x == 'L' else 1 for x in list(input[0])]
nodes = [x.replace('(','') for x in input[2:]]
nodes = [x.replace(')','') for x in nodes]
nodes = [x.replace(',','') for x in nodes]
nodes = [x.split('=') for x in nodes]

adaList = {}
for (source, destinations) in nodes:
    left, right = destinations.strip().split()
    source = source.strip()
    adaList[source] = (left, right)

steps = 0
curr = "AAA"
i = 0
while curr != "ZZZ":
    curr = adaList[curr][instructions[i]]
    i += 1
    i %= len(instructions)
    steps += 1
print(steps)