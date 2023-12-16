# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split(',')
# Close the file before we start solving.
input_file.close()

class advent_hash_map():
    buckets = []
    def __init__(self):
        self.buckets = [[] for _ in range(256)]

    def hash(self,s):
        num = 0 

        for l in s:
            num += ord(l)
            num *= 17
            num %= 256
        return num

    def insert(self,label,lens):
        box = self.buckets[self.hash(label)]
        for i in range(len(box)):
            if box[i][0] == label:
                box[i] = (label,lens)
                return
        box.append((label,lens))

    def remove(self,label):
        box = self.buckets[self.hash(label)]
        for i in range(len(box)):
            if box[i][0] == label:
               box.pop(i)
               break
    def print_buckets(self):
        for i,bucket in enumerate(self.buckets):
            if bucket: print(f"{i}:{bucket}")

    def calculuate_focusing_power(self):
        total_power = 0
        for i,box in enumerate(self.buckets):
            for j,(_,lens) in enumerate(box):
                power = (i+1)*(j+1)*lens
                total_power += power
        return total_power

advent_map = advent_hash_map()
for op in input:
    if "=" in op:
        label,lens = op.split("=")
        advent_map.insert(label,int(lens))
    else:
        advent_map.remove(op[:-1])

print(advent_map.calculuate_focusing_power())