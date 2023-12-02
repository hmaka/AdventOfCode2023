# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.readlines()
# Close the file before we start solving.
input_file.close()

# Remove commas.
input = [x.replace(',','') for x in input]
# Remove "Game n:".
input2 = [x.split(':')[-1][:-1] for x in input]
# Split every game (line) by round.
input2 = [x.split(';') for x in input2]

# Split every round by whitespace 
input3 = []
for i in range(len(input2)):
    temp = [ x.split() for x in input2[i]]
    input3.append(temp) 

summ = 0
minimum_set = []
for id, game in enumerate(input3):
    possible = True

    curr_min = [0,0,0]
    for round in game:
        for i in range(0,len(round),2):
            amount, color = int(round[i]), round[i+1]
            
            match color:

                case "red":
                    curr_min[0] = max(curr_min[0], amount)
                    if amount > 12:
                        possible = False
                case "blue":
                    curr_min[1] = max(curr_min[1], amount)
                    if amount > 14:
                        possible = False
                case "green":
                    curr_min[2] = max(curr_min[2], amount)
                    if amount > 13:
                        possible = False
    summ += id + 1 if possible else 0
    minimum_set.append(curr_min)

product_set = [r*b*g for [r,b,g] in minimum_set]
print(summ)
print(sum(product_set))
