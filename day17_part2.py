# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()

grid = [list(map(int,x)) for x in input]

def pprint(x):
    print()
    for r in x:
        print(r)

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

from heapq import heapify, heappush, heappop
seen = set()
pque = []
heapify(pque)
heappush(pque, (0,(0,0),RIGHT,0))
heappush(pque, (0,(0,0),DOWN,0))
# state_tupe := (heatloss, pos, heading, trav)
# heatloss := int, pos = (i,j), heading in [UP,DOWN,LEFT,RIGHT], Trav := int
while pque:
    heat_loss,(i,j),heading,trav = heappop(pque)
    if (i,j) == (len(grid)-1,len(grid[-1])-1) and trav > 3 :
        print(heat_loss)
        break

    seen_state = ((i,j),heading,trav)
    if seen_state in seen: continue
    seen.add(seen_state)
    for dir in [UP,DOWN,LEFT,RIGHT]:
        y,x = i+dir[0], j+dir[1]
        if x < 0 or x >= len(grid) or y<0 or y>= len(grid[x]): continue
        if dir == heading and trav < 10:
            heappush(pque,(heat_loss + grid[y][x], (y,x), dir, trav + 1))
        elif dir != heading and (dir != (-heading[0],-heading[1])) and trav > 3:
            heappush(pque, (heat_loss + grid[y][x], (y,x), dir, 1))
