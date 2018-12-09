import re
import string

def printArr(x):
  for i in x:
    print(i)

def solution1(player_count, last_marble): 

	# holds scores
	players = [0] * player_count

	# initialize other iterator variables
	circle = [0]
	current_position_idx = 0
	marble_num = 0
	player_num = -1 # //first move doesn't count towards any player

	# loop
	while True:
		#print(player_num+1, circle) #players are zero indexed, but want to match the sample output when i print here
		
		# base case, check for exit
		if marble_num == last_marble: return max(players)

		# otherwise, iterate on
		marble_num += 1
		player_num = (player_num + 1) % player_count

		# handle mod 23 case
		if marble_num % 23 == 0:
			current_position_idx = (current_position_idx - 7) % len(circle)
			score = marble_num + circle[current_position_idx]
			circle.pop(current_position_idx)
			players[player_num] += score
			continue;

		# else, normal play
		current_position_idx = (current_position_idx + 2) % len(circle)
		if current_position_idx == 0: current_position_idx = len(circle)
		circle.insert(current_position_idx, marble_num)



## Load input data and run our two main functions
if __name__ == '__main__':
  with open('../puzzle-input/day9_2018.txt', 'r') as file:
    inpt_lines = file.read().splitlines()

  tokens = inpt_lines[0].split(' ')
  player_count = 462 #int(tokens[0])
  last_marble = 71938 #int(tokens[6])	
  print( solution1(player_count, last_marble) )
  print( solution1(player_count, last_marble * 100) )
