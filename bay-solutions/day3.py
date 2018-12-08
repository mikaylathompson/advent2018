
import re

def solution1(inpt_lines):  
  grid = [[0] * 1000 for i in range(1000)] # may need to be larger, "at least 1k inches.. tbd"

  #example: #10 @ 359,82: 26x23
  for line in inpt_lines:
    tokens = list(filter(None, re.split('\s|#|@|,|:|x', line)))
    row = int(tokens[1])
    col = int(tokens[2])
    row_step = int(tokens[3])
    col_step = int(tokens[4])

    for i in range(row, row+row_step):
      for y in range(col, col+col_step):
        grid[i][y] += 1
    
  # countem
  results = 0
  for row in grid:
    for square in row:
      results += (square > 1)
  return results


def solution2(inpt_lines):
  grid = [[0] * 1000 for i in range(1000)] # may need to be larger, "at least 1k inches.. tbd"

  # draw once
  for line in inpt_lines:
    tokens = list(filter(None, re.split('\s|#|@|,|:|x', line)))
    row = int(tokens[1])
    col = int(tokens[2])
    row_step = int(tokens[3])
    col_step = int(tokens[4])
    for i in range(row, row+row_step):
        for y in range(col, col+col_step):
          grid[i][y] += 1

  # now go back and find unique
  for line in inpt_lines:
    tokens = list(filter(None, re.split('\s|#|@|,|:|x', line)))
    row = int(tokens[1])
    col = int(tokens[2])
    row_step = int(tokens[3])
    col_step = int(tokens[4])

    overlap_flag = False
    for i in range(row, row+row_step):
      for y in range(col, col+col_step):
        overlap_flag = overlap_flag or (grid[i][y] > 1)
    
    if not(overlap_flag): return line 


## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day3_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  print( solution1(inpt_lines) )
  print( solution2(inpt_lines) )
