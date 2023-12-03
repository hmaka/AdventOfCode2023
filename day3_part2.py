# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.readlines()
# Close the file before we start solving.
input_file.close()


grid = [x.replace('\n','') for x in input]


def process(grid, gear_box, num, i:int , j:int) -> bool:
    found_symbol = False
    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
    for dir in directions:
        y = i + dir[0]
        x = j + dir[1]
        
        if (y >= 0 and y < len(grid) and 
            x >= 0 and x < len(grid[y]) and 
            not grid[y][x].isnumeric() and 
            grid[y][x] != '.'):
            if grid[y][x] == '*':
                if (y,x) not in gear_box:
                    gear_box[(y,x)] = [1, num]
                else:
                    gear_box[(y,x)][0] += 1
                    gear_box[(y,x)][1] *= num
            found_symbol = True

    return found_symbol 

gear_box = {}
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
            if process(grid, gear_box, num, i, l):
                summ += num
                break
        j = k - 1
        j += 1
gear_box = [gear[1] for gear in gear_box.values() if gear[0] == 2]
print(sum(gear_box))

print(summ)
