# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.read().strip().split('\n')
# Close the file before we start solving.
input_file.close()
from dataclasses import dataclass
from collections import deque
def pprint(x):
    for r in x:
        print(r)

@dataclass
class Flip_flop_module:
    name: str
    children: list
    state: bool
    def __init__(self,name, children = []) -> None:
        self.name = name
        self.children = children
        self.state = False

    def pulse(self,q:deque, pulse: bool):
        if pulse : return
        self.state = not self.state
        for child in self.children:
            q.append((child,self.state, self.name))

@dataclass
class Conjunction_module:
    name: str
    parents: dict
    children: list
    state: bool
    def __init__(self, name, children = []) -> None:
        self.name = name
        self.children = children
        self.state = False
        self.parents = {}
    def pulse(self, q:deque, pulse:bool, parent:str):
        self.parents[parent] = pulse
        for child in self.children:
            q.append((child, any(not x for x in self.parents.values()), self.name))

broadcast = input.pop(0)
broadcast = [x.strip() for x in broadcast.split('->')[1].strip().split(',')]
adaMap = {}

for line in input:
    module_info,rest = line.split("->")
    module_type,module_name = module_info[0],module_info[1:].strip()

    children = [x.strip() for x in rest.split(",")]
    module = None 
    match module_type:
        
        case "%":
            module = Flip_flop_module(module_name, children)
        
        case "&":
            module = Conjunction_module(module_name, children)
    adaMap[module.name] = module

# populate parents of conjunction modules

conjuc_list = [x for x in adaMap.values() if isinstance(x, Conjunction_module)]

for c in conjuc_list:
    parents = []
    for module in adaMap.values():
        if c.name in module.children: parents.append(module.name)
    c.parents = {key:False for key in parents}

for b in broadcast:
    module = adaMap[b]
    if isinstance(module, Conjunction_module): module.parents["broadcast"]


low_pulses = 0
high_pulses = 0
# begin simulation
pulse_queue = deque() 
for i in range(1000):

    low_pulses += 1 
    for b in broadcast:
        pulse_queue.append((b, False, "broadcaster"))

    while pulse_queue:
        send_name,pulse,prev = pulse_queue.popleft()
        if pulse: high_pulses += 1
        else: low_pulses += 1
        module: Conjunction_module | Flip_flop_module = adaMap.get(send_name)
        if not module: continue
        if isinstance(module, Conjunction_module): module.pulse(pulse_queue, pulse, prev)
        else: module.pulse(pulse_queue, pulse)

print(low_pulses*high_pulses)