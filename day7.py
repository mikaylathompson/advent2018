from collections import defaultdict, OrderedDict
from pprint import pprint
import string

def process_deps(inpt_lines):
    # Make a dictionary of steps with a list of all their dependencies
    # Sort it (deal with the alphabetical thing)
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

    return sorted_steps, allsteps

def fn1(inpt_lines):
    # Search for any available steps and add to a 'completed' list.
    # And then run a loop that goes through the list to find anything that's available.
    sorted_steps, allsteps = process_deps(inpt_lines)

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
    base_time = 60
    n_workers = 5
    extra_time = {l:i+1 for i, l in enumerate(string.ascii_uppercase)}
    # Workers array has the current task and the countdown to completing it.
    workers = [(None, 0)] * n_workers

    sorted_steps, allsteps = process_deps(inpt_lines)
    def count_down(timers):
        return [(s, t - 1 if t > 0 else 0) for s, t in timers]
    def next_available_worker(workers):
        for i, (step, _) in enumerate(workers):
            if step is None:
                return i
        return None

    # (my handling of the timer is a little fudgy to get it to line up with the examples, but it works.)
    time = -2
    completed = OrderedDict()
    while len(allsteps) > 0 or not all(s is None for s,_ in workers):
        workers = count_down(workers)
        time += 1
        print("{0}\t{1}\t\t{2}".format(time, workers, ''.join(completed.keys())))

        # Deal with just-finished steps.
        for i, (step, timer) in enumerate(workers):
            if timer <= 0 and step is not None:
                completed[step] = True
                workers[i] = (None, 0)

        # Check if there are any available workers:
        next_worker = next_available_worker(workers)
        if next_worker is None:
            continue

        for step, deps in sorted_steps:
            if step not in allsteps:
                continue
            if all(d in completed for d in deps):
                # DON'T add the step to the completed list.
                # Instead, assign it to a worker.
                workers[next_worker] = (step, base_time + extra_time[step])
                # and pop it out of allsteps
                allsteps.discard(step)
                # Need to keep going through the list if there are more available workers.
                next_worker = next_available_worker(workers)
                if next_worker is None:
                    # No workers, need to go to next time period
                    break
                else:
                    continue

    return ''.join(completed.keys()), time+1

if __name__ == '__main__':
    with open('day7.txt', 'r') as inpt:
        print(fn1(inpt.readlines()))
        inpt.seek(0)
        print(fn2(inpt.readlines()))
