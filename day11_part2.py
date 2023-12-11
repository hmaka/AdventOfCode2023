# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()

def pprint(listt):
    for r in listt:
        print(r)

input = [list(row) for row in input]

row_expansions = []
col_expansions = []

galaxy_counter = 1
galaxy_locations = []
for i in range(len(input)):
    if "#" not in input[i]:
        row_expansions.append(i)


input2 = list(zip(*input))
input2 = [list(x) for x in input2]

for i in range(len(input2)):
    if "#" not in input2[i]:
        col_expansions.append(i)

input = list(zip(*input2))
input = [list(x) for x in input]

print(row_expansions)
print(col_expansions)

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            input[i][j] = str(galaxy_counter)
            galaxy_counter += 1
            galaxy_locations.append((input[i][j], (i,j)))

def account_expansion(x1,x2, type):
    x1, x2 = min(x1,x2), max(x1,x2)
    expanded = None

    match type:
        case "row": expanded = row_expansions
        case "col": expanded = col_expansions
        case _: raise RuntimeError("wrong type passed")

    intersection = [x for x in expanded if x > x1 and x < x2]
    return (1000000 - 1)*len(intersection)


ans = 0
for start_galaxy in galaxy_locations:
    galaxy, location = start_galaxy
    for i in range(int(galaxy),len(galaxy_locations)):
        y1,x1 = location
        y2,x2 = galaxy_locations[i][1]
        distance = abs(y2 - y1) + abs(x2 - x1) + account_expansion(y1,y2,"row") + account_expansion(x1,x2,"col")
        ans += distance

print(ans)