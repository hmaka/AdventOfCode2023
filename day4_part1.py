# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split("\n")
# Close the file before we start solving.
input_file.close()

winning_nums, owned_nums = [],[] 

for row in input:
    temp = row.split("|")
    winning_nums.append(temp[0].strip().split())
    owned_nums.append(temp[1].strip().split())

summ = 0
for w,o in zip(winning_nums,owned_nums):
    wins = len(set(w) & set(o))
    points = 0 if not wins else 2**(wins-1)
    summ += points

print(summ)
