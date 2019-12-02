
def solution1(inpt_lines):
  two_count = 0
  three_count = 0

  for line in inpt_lines:
    abc_counts = [0] * 26
    for letter in line:
      letter_index = ord(letter) - 97
      abc_counts[ letter_index ] += 1

    two_flag = False
    three_flag = False
    for l in abc_counts:
      if l==2: two_flag = True
      if l==3: three_flag = True

    if two_flag: two_count += 1
    if three_flag: three_count += 1

  checksum = two_count * three_count
  return checksum


def solution2(inpt_lines):
  line_length = len(inpt_lines[0])

  for i in range(0,line_length):
    seen = set()
    for line in inpt_lines:
      slug = line[:i] + line[i+1:]
      if slug in seen: return slug
      seen.add(slug)

  return 


## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day2_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  print( solution1(inpt_lines) )
  print( solution2(inpt_lines) )
