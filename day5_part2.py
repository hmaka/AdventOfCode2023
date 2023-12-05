# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()




seeds = [int(x) for x in input[0].split(':')[-1].strip().split()]
maps = []

input = [x for x in input if x != '']

i = 1

while i < len(input):
    if not input[i][0].isdigit():
        i += 1
    mapp = []
    while i < len(input) and input[i][0].isdigit():
        mapp.append([int(x) for x in input[i].split()])
        i += 1
    maps.append(mapp)

def find_instersection(range1, range2):
    l1,r1 = range1
    l2,r2 = range2
    if ((r1 < l2) or  (r2 < l1)): return None
    l = max(l1, l2) 
    r = min(r1, r2)
    return (l,r)

def find_all_complements(r1, ranges):
    if not ranges: return [r1]
    ranges.sort()
    ranges.append((r1[1]+1,r1[1]+1)) 
    complement_ranges = []
    ptr = r1[0]
    for range in ranges:
        if ptr < range[0]:
            complement_ranges.append((ptr,range[0]-1))
        ptr = range[1] + 1 
    return complement_ranges

def mapper(mappings, input):
    # mappings := [mapp]
    # mapp := [domain, range, span]
    # input := (start, end) (inclusive)
    pre_images = []
    output_ranges = []
    for mapp in mappings:
        start_range, start_domain, span = mapp
        end_domain = start_domain + span
        intersection = find_instersection(input,(start_domain,end_domain))
        if not intersection: continue
        pre_images.append(intersection)
        temp = (start_range + intersection[0] - start_domain, start_range + end_domain - intersection[1])
        output_ranges.append(temp)

    output_ranges.extend(find_all_complements(input,pre_images))
    output_ranges.sort() 
    return output_ranges


mapped_seed_ranges = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0,len(seeds),2)]

for mapping in maps:
    temp = []
    for seed_range in mapped_seed_ranges:
        temp.extend(mapper(mapping, seed_range))
    mapped_seed_ranges = temp

mapped_seed_ranges.sort()
print(mapped_seed_ranges, min(mapped_seed_ranges))