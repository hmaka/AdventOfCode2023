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


RIGHT = (0,1)
LEFT = (0,-1)
DOWN = (1,0)
UP = (-1,0) 

grid = input
from collections import deque

# state tuple := (pos,dir)
# pos := (i,j)
# dir in [RIGHT,LEFT,DOWN,UP]

start = ((0,-1),RIGHT)
que = deque()
seen = set()

que.append(start)
seen.add(start)

while que:
    (i,j),dir = que.popleft()
    i,j = i + dir[0], j+dir[1]

    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]): continue

    next_states = []
    match grid[i][j]:
        case ".":
            next_states.append( ((i,j),dir) )
        case "|":
            if dir == LEFT or dir == RIGHT:
                temp = [((i,j),UP),((i,j),DOWN)]
                next_states.extend(temp)
            else: 
                next_states.append( ((i,j),dir) )
        case "-":
            if dir == UP or dir == DOWN:
                temp = [((i,j),LEFT), ((i,j),RIGHT)]
                next_states.extend(temp)
            else: 
                next_states.append( ((i,j),dir) )
 
        case "\\":
            next_states.append(((i,j), (dir[1],dir[0])))
        case "/":
            next_states.append(((i,j), (-dir[1],-dir[0])))
    

    assert(len(next_states) > 0)
    for state in next_states:
        if state not in seen:
            seen.add(state)
            que.append(state)

energized = {pos for (pos,_) in seen}
print(len(energized)-1)
    # right -> / = up   (0,1) -> (-1,0) 
    # left -> / = down (0,-1) -> (1,0)
    # down -> / = left (1,0) -> (0,-1)
    # up -> / = right
    # formula := dir[0],dir[1] = -dir[1], -dir[0]

    # right -> \ = down (0,1) -> (1,0)
    # left -> \ = up (0,-1) -> (-1,0)
    # down -> \ = right
    # up -> \ = left
    # formula := dir[0],dir[1] = dir[1],dir[0]