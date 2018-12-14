import re
import string
from collections import defaultdict
import pprint

def build_dict(match_lines):
    d = defaultdict(bool)
    for line in match_lines:
        inpt, outpt = line.strip().split(' => ')
        d[inpt] = (outpt == '#') # gives a bool
    return d

def spawn(state, mapping):
    ns = list() #('..')
    for i, char in enumerate(state[2:-2]):
        # print(state[i-2:i+3], mapping[state[i-2:i+3]] )
        ns.append('#' if mapping[state[i-2:i+3]] else '.')
    return ''.join(ns + list('....'))

def sum_values(state, zero_point):
    return sum([i - zero_point for i, char in enumerate(state) if char == "#"])
    # s = 0
    # for i, char in enumerate(state):
    #     if char == "#":
    #         s += i - zero_point
    # return s

def fn1(inpt_lines): 
    GENS = 20
    # GENS = 3
    initial = inpt_lines[0].strip().split(': ')[1]
    zero_point = len(initial)
    mapping = build_dict(inpt_lines[2:])

    state = ('.' * zero_point) + initial + ('.' * zero_point)
    # print(state[zero_point])
    for i in range(GENS):
        # print(f"{i}\t{state[:zero_point]}|{state[zero_point:2*zero_point]}|{state[2*zero_point:]}")
        state = spawn(state, mapping)

    # print(f"{i+1}\t{state[:zero_point]}|{state[zero_point:2*zero_point]}|{state[2*zero_point:]}")

    return sum_values(state, zero_point)

def fn2(inpt_lines):
    # 278 is TOO LOW

    # must rely on looking for loops
    # GENS = 50000000000
    GENS = 140
    seen_positions = {}

    initial = inpt_lines[0].strip().split(': ')[1]
    zero_point = len(initial)
    mapping = build_dict(inpt_lines[2:])
    state = ('.' * zero_point) + initial + ('.' * zero_point * 5)

    # print(state[zero_point])
    for i in range(GENS):
        if i > 100:
            print(f"{i}\t{sum_values(state, zero_point)}")
        # if state in seen_positions:
        #     print(f"Repeat found! At gen{i}, repeat of gen{seen_positions[state]}.")
        #     print(sum_values(state, zero_point))
        #     break
        # seen_positions[state] = i
        state = spawn(state, mapping)

    print(f"{i+1}\t{state[:zero_point]}|{state[zero_point:2*zero_point]}|{state[2*zero_point:]}")
    return sum_values(state, zero_point)

## Load input data and run our two main functions
if __name__ == '__main__':
    with open('../puzzle-input/day12_2018.txt', 'r') as f:
        inpt_lines = f.read().splitlines()

    print(fn1(inpt_lines))
    print(fn2(inpt_lines))
