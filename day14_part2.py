# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()


grid = [list(x) for x in input]

UP = (-1,0)
LEFT = (0,-1)
DOWN = (1,0)
RIGHT = (0,1)

def pprint(x):
    print()
    for r in x:
        print("".join(r))
    print()

def north_weight(grid):
    weight = 0
    for i,row in enumerate(grid):
        for element in row:
            if element == "O": weight += len(grid)-i
    print(weight)


def roll(i,j,dir, grid):
    k,l = i + dir[0], j+dir[1]

    while k >=0 and k < len(grid) and l >= 0 and l < len(grid[k]) and grid[k][l] not in "#O":
        k,l = k+dir[0],l+dir[1]
    
    if grid[k-dir[0]][l-dir[1]] not in "#O":
        grid[i][j] = "."
        grid[k-dir[0]][l-dir[1]] = "O"

def cycle(grid):
    for dir in (UP,LEFT):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "O": roll(i,j,dir,grid)

    for dir in (DOWN,RIGHT):
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[i])-1,-1,-1):
                if grid[i][j] == "O": roll(i,j,dir,grid)


def tupify(grid):
    return tuple(tuple(x) for x in grid)
seen = set()
order = []
hashable_grid = None

while True:
    hashable_grid = tupify(grid)
    if hashable_grid in seen: break
    seen.add(hashable_grid)
    order.append(hashable_grid)
    cycle(grid)

first_seen = order.index(hashable_grid)

end_state = order[(1000000000-first_seen)%(len(order) - first_seen) + first_seen]

north_weight(end_state)
