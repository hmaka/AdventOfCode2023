# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n\n')
# Close the file before we start solving.
input_file.close()

def pprint(x):
   print() 
   for r in x:
      print(r)  
   print()

def difference_is_one(grid1, grid2):
    diff_cnt = 0
    for r1, r2 in zip(grid1,grid2):
        for a,b in zip(r1,r2):
            if a != b: diff_cnt += 1
        if diff_cnt > 1: break

    return True if diff_cnt == 1 else False

def calculuate_reflection(grid):

    for i in range(1,len(grid)):
        upper = grid[:i]
        lower = grid[i:]

        if upper[::-1][:len(lower)] == lower[:len(upper)]: return i

    return 0
ans = 0
for block in input:
    grid = [list(x) for x in block.split('\n')]

    grid_transpose = list(zip(*grid))
    ans += 100*calculuate_reflection(grid)
    ans += calculuate_reflection(grid_transpose)

print(ans)