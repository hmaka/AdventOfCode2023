# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split(',')
# Close the file before we start solving.
input_file.close()

def hash(s):
    num = 0 

    for l in s:
        num += ord(l)
        num *= 17
        num %= 256
    return num

print(sum(hash(s) for s in input))

