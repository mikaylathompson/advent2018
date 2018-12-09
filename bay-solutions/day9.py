import re
import string

def printArr(x):
  for i in x:
    print(i)

#462 players; last marble is worth 71938 points
def solution1(inpt_lines): 
	tokens = inpt_lines[0].split(' ')
	player_count = 98# 462 #int(tokens[0])
	last_marble_score = 146373 #71938 #int(tokens[6])


	# holds scores
	players = [0] * player_count

	# initialize other iterator variables
	circle = [0]
	current_position_idx = 0
	marble_num = 0
	player_num = -1 # //first move doesn't count towards any player

	# loop
	while True:
		print(player_num+1, circle) #players are zero indexed, but want to match the sample output when i print here

		marble_num += 1
		player_num = (player_num + 1) % player_count

		# handle mod 23 case
		if marble_num % 23 == 0:
			current_position_idx = (current_position_idx - 7) % len(circle)
			score = marble_num + circle[current_position_idx]
			circle.pop(current_position_idx)
			players[player_num] += score
			if score == last_marble_score: return players[player_num]
			continue;

		# else, normal play
		current_position_idx = (current_position_idx + 2) % len(circle)
		if current_position_idx == 0: current_position_idx = len(circle)
		circle.insert(current_position_idx, marble_num)




def solution2(inpt_lines):
  return 0

## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day9_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  print( solution1(inpt_lines) )
  print( solution2(inpt_lines) )
