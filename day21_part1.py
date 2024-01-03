# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()

from collections import deque

que = deque()
seen = set()
#state tuple:= (i,j) 
(start_pos,) = [(i,j) for i in range(len(input)) for j in range(len(input[0])) if input[i][j] == "S"]

que.append((start_pos,0))
seen.add(start_pos)
end_spots = 0
while que:
    (i,j),steps = que.popleft()
    if steps % 2 == 0: end_spots +=1
    if steps == 64: continue
    for i2, j2 in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        if (i2 < 0 or i2 >= len(input) or j2 < 0 or j2 >= len(input[i]) or input[i2][j2] == "#" 
        or (i2,j2) in seen): continue
        que.append(((i2,j2),steps+1))
        seen.add((i2,j2))

print(end_spots)



