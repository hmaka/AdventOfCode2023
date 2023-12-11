
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

to_insert_empty_row = []
to_insert_empty_col = []
galaxy_counter = 1
galaxy_locations = []
for i in range(len(input)):
    if "#" not in input[i]:
        to_insert_empty_row.append(i)

for i in range(len(to_insert_empty_row)):
    input.insert(to_insert_empty_row[i], ["."]*len(input[0]))
    for j in range(i,len(to_insert_empty_row)):
        to_insert_empty_row[j] += 1

input2 = list(zip(*input))
input2 = [list(x) for x in input2]

for i in range(len(input2)):
    if "#" not in input2[i]:
        to_insert_empty_col.append(i)


for i in range(len(to_insert_empty_col)):
    input2.insert(to_insert_empty_col[i], ["."]*len(input2[0]))
    for j in range(i,len(to_insert_empty_col)):
        to_insert_empty_col[j] += 1

input = list(zip(*input2))
input = [list(x) for x in input]

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            input[i][j] = str(galaxy_counter)
            galaxy_counter += 1
            galaxy_locations.append((input[i][j], (i,j)))

ans = 0
for start_galaxy in galaxy_locations:
    galaxy, location = start_galaxy
    for i in range(int(galaxy),len(galaxy_locations)):
        y1,x1 = location
        y2,x2 = galaxy_locations[i][1]
        distance = abs(y2 - y1) + abs(x2 - x1)
        ans += distance

print(ans)
        
