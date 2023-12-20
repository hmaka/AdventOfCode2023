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

    def process_part(self, part)-> str:

        for rule,loc in self.rules:
            if rule[0] in part.keys():
                if "<" in rule:
                    c,val = rule.split("<")
                    if part[c] < int(val): return loc
                else:
                    c,val = rule.split(">")
                    if part[c] > int(val): return loc

        return self.terminal

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

accepted_parts = []
for part in parts:
    curr = adaMap["in"].process_part(part)
    while curr not in "AR":
        curr = adaMap[curr].process_part(part)
    if curr == "A": accepted_parts.append(part)

print(sum(sum(part.values()) for part in accepted_parts))





