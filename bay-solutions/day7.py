import re

def printArr(x):
  for i in x:
    print(i)

def solution1(inpt_lines): 

  order = ""

  # initialize main dict
  abc = {}
  for l in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    abc[l.upper()] = set()

  # build list of blockers for each letter
  for line in inpt_lines:
    tokens = line.split(' ')
    abc[tokens[7]].add( tokens[1] )

  # iterate through alphabet in order, choosing first letter w/o blockers
  while len(abc)>0:
    for l, blockers in sorted(abc.items()):
      if not blockers: 

        # add to our string, then pop it out of nested sets so it's no longer a blocker!
        order += l
        abc.pop(l)
        for j in abc:
          abc[j].discard(l)
        break # important to now start again from top of alphabet, because you've made changes

  return order

def solution2(inpt_lines):
  return 0


## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day7_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  print( solution1(inpt_lines) )
  print( solution2(inpt_lines) )
