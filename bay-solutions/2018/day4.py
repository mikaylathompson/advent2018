import re

def printArr(x):
  for i in x:
    print(i)

def solution1(inpt_lines): 
  inpt_lines.sort() 
  #printArr(inpt_lines)

  # dictionary of {guard_id : [len 60 int array]} that will hold sleeping patterns as an int map
  guard_set = {}

  # iterate over all lines, recording sleep patterns
  for line in inpt_lines:
    tokens = list(filter(None, re.split('\s|\[|\]|\:|\-|\#', line)))
    
    if tokens[5] == 'Guard': 
      guard = int(tokens[6])
      if not(guard_set.get(guard)): guard_set[guard] = [0]*60  #initialize 60 min int map per guard

    if tokens[5] == 'falls':
      falls_time = int(tokens[4])

    if tokens[5] == 'wakes':
      wakes_time = int(tokens[4])
      for i in range(falls_time, wakes_time):
        guard_set[guard][i]+=1


  # now who slept the most?
  sleep_totals = dict()
  for guard, sleep_map in guard_set.items():
    sleep_totals[guard] = sum(sleep_map)
  max_guard_id = max(sleep_totals, key=sleep_totals.get)  

  # and when were they most likely sleeping?
  minute_max = guard_set[max_guard_id].index(max(guard_set[max_guard_id])) 

  # wrap up
  #print(max_guard_id)
  #print(sleep_totals[max_guard_id])
  #print(minute_max)
  return  max_guard_id * minute_max

def solution2(inpt_lines):
  inpt_lines.sort() 
  #printArr(inpt_lines)

  # dictionary of {guard_id : [len 60 int array]} that will hold sleeping patterns as an int map
  guard_set = {}

  sleepy_guard_id = 0 #id of guard with highest single min frequency
  sleepy_guard_minute = 0 #what minute that was
  sleepy_guard_freq_max = 0 #the freq of that minute

  # iterate over all lines, recording sleep patterns
  for line in inpt_lines:
    tokens = list(filter(None, re.split('\s|\[|\]|\:|\-|\#', line)))
    
    if tokens[5] == 'Guard': 
      guard = int(tokens[6])
      if not(guard_set.get(guard)): guard_set[guard] = [0]*60  #initialize 60 min int map per guard

    if tokens[5] == 'falls':
      falls_time = int(tokens[4])

    if tokens[5] == 'wakes':
      wakes_time = int(tokens[4])
      for i in range(falls_time, wakes_time):
        guard_set[guard][i]+=1

        # for section 2
        if guard_set[guard][i] > sleepy_guard_freq_max:
          sleepy_guard_id = guard
          sleepy_guard_minute = i
          sleepy_guard_freq_max = guard_set[guard][i]

  # wrap up
  return  sleepy_guard_id * sleepy_guard_minute


## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day4_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  print( solution1(inpt_lines) )
  print( solution2(inpt_lines) )
