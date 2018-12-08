import re

def printArr(x):
  for i in x:
    print(i)

def solution1(inpt_lines): 

  # load points
  pts = []
  for l in inpt_lines:
    x = int(l.split(',')[0])
    y =  int(l.split(',')[1])
    pts.append([x,y])

  # create big enough grid
  x_max = max(pts, key=lambda p: p[0])[0]
  y_max = max(pts, key=lambda p: p[1])[1]

  grid = []
  for r in range(0,x_max):
    row = []
    for c in range(0,y_max):
      row.append([9999,-1])
    grid.append(row)

  # fill in grid with closest point labels 
  #    (where label == pt index in pts array)
  for pt_idx, pt in enumerate(pts):
    for r in range(0,x_max):
      for c in range(0, y_max):
        distance = abs(pt[0]-r)+abs(pt[1]-c)
        if distance < grid[r][c][0]:
          grid[r][c][0] = distance
          grid[r][c][1] = pt_idx 
  
  # create a new 1D array where each cell will get added up to be the total land area of that pt index
  pt_areas = [0] * len(pts)
  for r in range(0, x_max):
    for c in range(0, y_max): 
      pt_areas[ grid[r][c][1] ] += 1

  # now figure out who is infinite so we can ignore them
  # (any pt whose area touches an edge will be infinite)
  infinite_pt_indexes = set()
  for r in range(0,x_max):
    infinite_pt_indexes.add(grid[r][0][1])
    infinite_pt_indexes.add(grid[r][y_max-1][1])
  for c in range(0, y_max):
    infinite_pt_indexes.add(grid[0][c][1])
    infinite_pt_indexes.add(grid[x_max-1][c][1])

  for i in infinite_pt_indexes:
    pt_areas[i] = -1

  return max (pt_areas)

def solution2(inpt_lines):

  # load points
  pts = []
  for l in inpt_lines:
    x = int(l.split(',')[0])
    y =  int(l.split(',')[1])
    pts.append([x,y])

  # create big enough grid
  x_max = max(pts, key=lambda p: p[0])[0]
  y_max = max(pts, key=lambda p: p[1])[1]

  # this time we initailize the grid with 0's, instead of [distance, pt_idx] tuples
  # the int at each coord in array will equal the sum of all pt-distances to that coord
  grid = []
  for r in range(0,x_max):
    row = []
    for c in range(0,y_max):
      row.append(0)
    grid.append(row)

  # fill in grid with distance from this point (adding on top of existing vals)
  for pt_idx, pt in enumerate(pts):
    for r in range(0,x_max):
      for c in range(0, y_max):
        distance = abs(pt[0]-r)+abs(pt[1]-c)
        grid[r][c] += distance  

  # count how many squares are safe
  safe_count = 0
  for r in range(0,x_max):
    for c in range(0, y_max):
      if grid[r][c]<10000: safe_count += 1

  return safe_count


## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day6_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  print( solution1(inpt_lines) )
  print( solution2(inpt_lines) )
