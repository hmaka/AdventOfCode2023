# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n\n')
# Close the file before we start solving.
input_file.close()
adaList, parts = input
adaList = adaList.split('\n')
parts = parts.split('\n')
# px{a<2006:qkq,m>2090:A,rfg}
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class workflow():
    name:str
    rules: list
    terminal: str

    def __init__(self, wf) -> None:
        self.name, rest = wf.split('{')
        rest = rest[:-1]
        rules = rest.split(',')
        self.terminal = rules[-1]
        rules = rules[:-1]
        self.rules = []
        for rule in rules:
            self.rules.append(tuple(rule.split(':')))

def parse_part(part):
# part:= {x=787,m=2655,a=1222,s=2876}
    part = part[1:-1]
    part = part.split(',')
    part = [x.split('=') for x in part]
    part = {catagory:int(rating) for (catagory,rating) in part}
    # part := [(catagory,rating),...]
    return part

parts = [parse_part(p) for p in parts]

adaList = [workflow(x) for x in adaList]
adaMap = {wf.name:wf for wf in adaList}

def recursive_range_finder(wf_name:str, ranges:dict):
    if wf_name== "A":
        ans = 1
        for range in ranges.values():
            ans *= range[1]-range[0] + 1
        return ans

    elif wf_name == "R": return 0
    wf = adaMap[wf_name]
    combs = 0
    ranges_copy = deepcopy(ranges)
    for rule in wf.rules:
         
        name,rule_range = None,None
        rule,send_to = rule
        if "<" in rule:
            name,num = rule.split("<")
            rule_range = (1,int(num)-1)
            rule_complement = (int(num), 4000)
        else:
            name,num = rule.split(">")
            rule_range = (int(num)+1,4000)
            rule_complement = (1,int(num))

        range = ranges_copy[name]
        intersection = (max(int(range[0]),rule_range[0]), min(int(range[1]),rule_range[1]))
        complement = (max(int(range[0]), rule_complement[0]), min(int(range[1]), rule_complement[1]))
        ranges_copy[name] = intersection
        
        combs += recursive_range_finder(send_to,ranges_copy)
        ranges_copy[name] = complement

    combs += recursive_range_finder(wf.terminal, ranges_copy)
    return combs

# range tuple := (x_range,m_range,a_range,s_range) := {'x':(1,4000), 'm':(1,4000), 'a': (1,4000), 's':(1,4000)} inclusive.
start_range = {'x':(1,4000), 'm':(1,4000), 'a': (1,4000), 's':(1,4000)}
print(recursive_range_finder("in", start_range))