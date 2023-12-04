# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()

from collections import deque
from functools import cache
winning_nums, owned_nums = [],[] 

for row in input:
    temp = row.split("|")
    winning_nums.append(temp[0].strip().split())
    owned_nums.append(temp[1].strip().split())

@cache
def process(row):
    w,o  = cards[row]
    wins = len(set(w) & set(o))
    
    return list(range(row+1,row+wins+1,1))
    
cards = list(zip(winning_nums, owned_nums))
done = []
queue = deque()

for i in range(len(cards)):
    queue.append(i)

while queue:
    process_row = queue.popleft()
    done.append(process_row)
    need_to_be_processed = process(process_row)
    queue.extend(need_to_be_processed)

print(len(done))
