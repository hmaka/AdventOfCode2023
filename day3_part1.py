# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.readlines()
# Close the file before we start solving.
input_file.close()

grid = [x.replace('\n','') for x in input]

def process(grid, i:int , j:int) -> bool:

    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
    for dir in directions:
        y = i + dir[0]
        x = j + dir[1]

        if (y >= 0 and y < len(grid) and 
            x >= 0 and x < len(grid[y]) and 
            not grid[y][x].isnumeric() and 
            grid[y][x] != '.'):

            return True 

    return False

summ = 0
for i in range(len(grid)):
    j = 0
    while j < len(grid[i]):

        if not grid[i][j].isdigit(): 
            j += 1
            continue
        
        k = j
        while k < len(grid[i]) and grid[i][k].isdigit(): k += 1
        num = int(grid[i][j:k])
        
        for l in range(j,k,1):
            if process(grid, i, l):
                summ += num
                break
        j = k - 1
        j += 1

print(summ)
        

        
