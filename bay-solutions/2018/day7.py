import re
import string

def printArr(x):
  for i in x:
    print(i)

def solution1(inpt_lines): 

  # this is the main ouput string we will build up and return
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

  # setup 5 empty workers
  # each worker represented by a tuple :
  #      0: --> letter under operation
  #      1: --> clock_cycles_remaining
  workers = []
  for i in range(0,5):
    workers.append([0,0])

  # initialize main dict that represents graph
  abc = {}
  for l in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    abc[l.upper()] = set()

  # build list of blockers for each letter
  for line in inpt_lines:
    tokens = line.split(' ')
    abc[tokens[7]].add( tokens[1] )

  # start main execution loop, run until all jobs are taken then you can bail
  clock_time = -1 # base case, so first loop can be time t=0
  while len(abc)>0: 

    # add a second to the clock, and decrease all worker cycles remaining
    clock_time += 1
    for w in workers:
      if w[0]: w[1] -= 1 # tick off a second, if this worker is active

      # finish the job for this worker if they are now at zero 
      if w[0] and w[1] == 0:
        for j in abc:
          abc[j].discard(w[0]) #job has finished, so remove from blocking list
        w[0] = 0 # free up worker

    # iterate through alphabet in order, choosing first letter w/o blockers
    for l, blockers in sorted(abc.items()):
      if not blockers: 

        # then find the next worker who is available
        worker = next(filter(lambda w: not(w[0]), workers))

        # assign this worker the job so no one else can have it
        worker[0] = l
        abc.pop(l)
        worker[1] = 60 + string.ascii_lowercase.index(l.lower())+1

  #     
  # now the final jobs just have to finish, so see time remaining, and add to total
  clock_time += max(workers, key=lambda p: p[1])[1]

  # you're done!
  return clock_time

## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day7_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  print( solution1(inpt_lines) )
  print( solution2(inpt_lines) )
