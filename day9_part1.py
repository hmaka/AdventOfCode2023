# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()

#print(len(input), len(input[0]))
def extrapolate_row(row):
    row = [int(x) for x in row.split()]
    curr = row.copy()
    last_nums = []
    while any(x != 0 for x in curr):
        temp = [curr[i] - curr[i-1] for i in range(1,len(curr),1)]
        last_nums.append(temp[-1])
        curr = temp

    return row[-1] + sum(last_nums)

print(sum(extrapolate_row(x) for x in input))