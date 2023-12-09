# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()

def extrapolate_row(row):
    row = [int(x) for x in row.split()]
    curr = row.copy()
    last_nums = []
    first_nums = []
    while any(x != 0 for x in curr):
        temp = [curr[i] - curr[i-1] for i in range(1,len(curr),1)]
        last_nums.append(temp[-1])
        first_nums.append(temp[0])
        curr = temp

    first_nums.pop()
    backwards_extrap = [0]
    for i in range(len(first_nums)-1,-1,-1):
        backwards_extrap.append(first_nums[i]-backwards_extrap[-1])
    backwards_extrap.append(row[0]-backwards_extrap[-1])

    return backwards_extrap[-1]

print(sum(extrapolate_row(x) for x in input))