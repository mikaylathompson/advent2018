def solution1(inpt_lines):
  current_val = 0
  for line in inpt_lines:
    if line[0] == '-':
      current_val -= int(line[1:])
    else:
      current_val += int(line[1:])
  return current_val


def solution1_alt(inpt_lines):
  eval_str = "0"
  for line in inpt_lines:
    eval_str += line
  return eval(eval_str)
 

def solution2(inpt_lines):
  current_val = 0
  seen_vals = set()
  while True:
    for line in inpt_lines:
      if line[0] == '-':
        current_val -= int(line[1:])
      else:
        current_val += int(line[1:])

      if current_val in seen_vals:
        return current_val
      seen_vals.add(current_val)


## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day1_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  print( solution1(inpt_lines) )
  print( solution1_alt(inpt_lines) )
  print( solution2(inpt_lines) )
