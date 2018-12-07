from collections import defaultdict, OrderedDict
from pprint import pprint

def fn1(inpt_lines):
    # Make a dictionary of steps with a list of all their dependencies
    # Sort it (deal with the alphabetical thing)
    # Search for any available steps and add to a 'completed' list.
    # And then run a loop that goes through the list to find anything that's available.
    unsorted_steps = defaultdict(set)
    allsteps = set()
    for line in inpt_lines:
        line = line.split()
        dependency = line[1]
        target = line[7]
        unsorted_steps[target].add(dependency)
        allsteps.add(target)
        allsteps.add(dependency)

    sorted_steps = [(step, unsorted_steps[step]) for step in sorted(allsteps)]

    # I don't actually care about the values at all, but I'm using an OrderedDict for constant-time lookup with ordering.
    completed = OrderedDict()

    while len(allsteps) > 0:
        for step, deps in sorted_steps:
            if step in completed:
                continue
            if all(d in completed for d in deps):
                # Add the step to the completed list.
                completed[step] = True
                # Pop it out of allsteps
                allsteps.discard(step)
                break
    return ''.join(completed.keys())

def fn2(inpt_lines):
    return None

if __name__ == '__main__':
    with open('day7.txt', 'r') as inpt:
        print(fn1(inpt.readlines()))
        inpt.seek(0)
        print(fn2(inpt.readlines()))
