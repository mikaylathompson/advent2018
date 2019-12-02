import math

def solution1(inpt_lines):
	total = 0
	for line in inpt_lines:
		total = total + math.floor(int(line)/3)-2
	return total


def solution2(inpt_lines):
	total = 0
	for line in inpt_lines:
		total = total + getGas(int(line))
	return total

def getGas(m):
	r = math.floor(int(m)/3)-2
	return 0 if r<=0 else (r + getGas(r))
	
## Load input data and run our two main functions
if __name__ == '__main__':
	with open('../../puzzle-input/day1_2019.txt', 'r') as file:
		inpt_lines = file.read().splitlines()

	print( solution1(inpt_lines) )
	print( solution2(inpt_lines) )

