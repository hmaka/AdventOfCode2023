# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()


def pprint(x):
    print()
    for r in x:
        print("".join(r))
    print()

grid = [list(x) for x in input]

def roll(i,j,grid):
    k = i-1
    while k >=0 and grid[k][j] not in "#O":
        k -= 1
    if grid[k+1][j] not in "#O":
        grid[i][j] = "."
        grid[k+1][j] = "O"

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "O": roll(i,j,grid)
        
weight = 0
for i,row in enumerate(grid):
    for element in row:
        if element == "O": weight += len(grid)-i
print(weight)