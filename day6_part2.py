# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()

times = [int(input[0].split(':')[1].strip().replace(" ",""))]

distances = [int(input[1].split(':')[1].strip().replace(" ",""))]

# You can use the quadratic equation to solve this, it's much faster and if the input was larger it would have been a must.

ans = 1
for time,distance in zip(times,distances):
    distances_traveled = []
    for i in range(time):
        speed = i
        time_remaining = time - i
        distances_traveled.append(speed*time_remaining)

    winning_distances = [x for x in distances_traveled if x > distance] 
    ans*= len(winning_distances) 

print(ans)
