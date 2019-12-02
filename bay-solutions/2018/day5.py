import re

def printArr(x):
  for i in x:
    print(i)

def solution1(inpt_lines): 
  polymer = inpt_lines[0]
  old_p = ''
  print(len(polymer))

  while old_p != polymer:
    old_p = polymer
    for l in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
      polymer = polymer.replace( l.upper()+l, "")
      polymer = polymer.replace( l+l.upper(), "")

  return len(polymer)

def solution2(inpt_lines):
  orig = inpt_lines[0]

  min_seen = 9999999999
  for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:

    polymer = orig
    polymer = polymer.replace(i,"")
    polymer = polymer.replace(i.upper(),"")

    old_p = ''
    while old_p != polymer:
      old_p = polymer
      for l in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        polymer = polymer.replace( l.upper()+l, "")
        polymer = polymer.replace( l+l.upper(), "")

    if len(polymer) < min_seen: min_seen = len(polymer)

  return min_seen 



## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day5_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  print( solution1(inpt_lines) )
  print( solution2(inpt_lines) )
