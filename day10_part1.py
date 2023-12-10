# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()



start = (0,0)
n,m = len(input), len(input[0])
for i in range(n):
    for j in range(m):
        if input[i][j] == 'S':
            start = (i,j)
            break
# up, right , down , left
UP = (-1,0)
RIGHT = (0,1)
DOWN = (1,0)
LEFT = (0,-1)

dist = [[0]*m for _ in range(n)]
seen = set()

going_pipe_compatible = {
    "-":set((LEFT,RIGHT)),
    "L":set((UP,RIGHT)),
    "|":set((UP,DOWN)),
    "J":set((UP,LEFT)),
    "F":set((RIGHT,DOWN)),
    "7":set((LEFT,DOWN)),
    "S":set((UP,RIGHT,DOWN,LEFT)),
    ".":()
}

incoming_pipe_compatible = {
    "-":set((LEFT,RIGHT)),
    "L":set((DOWN, LEFT)),
    "|":set((UP,DOWN)),
    "J":set((DOWN,RIGHT)),
    "F":set((LEFT,UP)),
    "7":set((RIGHT,UP)),
    "S":(),
    ".":()
}

import sys
sys.setrecursionlimit(10**6)

def dfs(i:int,j:int, curr_dist:int):
    if (i,j) in seen: return
    dist[i][j] = curr_dist if not dist[i][j] else min(dist[i][j], curr_dist)

    for dir in (UP,RIGHT,DOWN,LEFT):
        y,x = i+dir[0],j+dir[1]

        if (y < 0 or
            y >= n or 
            x < 0 or 
            x >= m): continue
        curr, next = input[i][j], input[y][x]
        if dir in going_pipe_compatible[curr] and dir in incoming_pipe_compatible[next]:
            seen.add((i,j))
            dfs(y,x, curr_dist + 1)
            seen.remove((i,j))

dfs(start[0],start[1], 0)
farthest = 0

for i in range(n):
    for j in range(m):
        farthest = max(farthest, dist[i][j])
print(farthest)
