import re
import string


# <3 global vars
GLOBAL_META_COUNT = 0

# Our node object. Pretty simple.
class Node:
  children = None
  meta = None
  def __init__(self):
    self.children = []
    self.meta = []

  def print(self):
    print(f"children: {len(self.children)}")
    print(f"meta: {self.meta}")

# processes the first (front) node in an array of numbers.
#    returns a pointer to new node object, including meta data and child nodes
#    calls itself recursively as needed (for child nodes)
#    removes (pops) items out of overall chain as it works to maintain single state
def process_node(nd):
  global GLOBAL_META_COUNT

  # remove first 2 vals, which specify num children and num meta
  child_count = int(nd.pop(0))
  meta_count = int(nd.pop(0))

  # create a new node structure
  new_node = Node()

  # recursively loop on child nodes if they exist  
  while child_count > 0:
    child_count -= 1
    new_node.children.append( process_node(nd) )

  #no more children, so now just process meta
  while meta_count > 0:
      meta_count -=1
      m = int(nd.pop(0))
      new_node.meta.append(m)
      GLOBAL_META_COUNT += m
  
  return new_node  


def solution1(inpt_lines): 
  global GLOBAL_META_COUNT
  GLOBAL_META_COUNT = 0
  
  arr = inpt_lines[0].split(' ')
  root_note = process_node(arr)
  return GLOBAL_META_COUNT


# 
# calculates the value of a node, as per solution2
# can be called recursively
def getNodeValue(nd):
  if len(nd.children) == 0:
    return sum(nd.meta)

  # otherwise, add up kids
  value = 0
  for m in nd.meta:
    if m > len(nd.children): continue
    value += getNodeValue(nd.children[ m-1 ])
  return value

def solution2(inpt_lines):
  arr = inpt_lines[0].split(' ')
  root_node = process_node(arr)
  val = getNodeValue(root_node)  
  return val




## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day8_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  #print( solution1(inpt_lines) )
  print( solution2(inpt_lines) )
