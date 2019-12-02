import re
import string

def printArr(x):
  for i in x:
    print(i)

def solution1(inpt_lines): 
  return 0

def solution2(inpt_lines):
  return 0

## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day14_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  print( solution1(inpt_lines) )
  print( solution2(inpt_lines) )
