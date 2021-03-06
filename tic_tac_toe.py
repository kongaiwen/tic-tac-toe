from random import randint
from time import sleep

def tic_tac_toe():
	# Organization of the game grid
	grid = [[" ", ".__1___.___2__.___3__."],
			[" ", "|  ", " ", " |  ", " ", " |  ", " ", " |"],
			["A", "|______|______|______|"],
			[" ", "|  ", " ", " |  ", " ", " |  ", " ", " |"],
			["B", "|______|______|______|"],
			[" ", "|  ", " ", " |  ", " ", " |  ", " ", " |"],
			["C", "|______|______|______|"]]

	# Winning Sets
	win_sets = [{(0,0), (1,1), (2,2)},
				{(2,0), (1,1), (0,2)},
				{(0,0), (0,1), (0,2)},
				{(1,0), (1,1), (1,2)},
				{(2,0), (2,1), (2,2)},
				{(0,0), (1,0), (2,0)},
				{(0,1), (1,1), (2,1)},
				{(0,2), (1,2), (2,2)}]

	# Winning coordinate pathways sets
	advantage_sets = {(0,0):{(1,1), (2,2), (0,1), (0,2), (1,0), (2,0)},
					(0,1):{(0,0), (0,2), (1,1), (2,1)},
					(0,2):{(2,0), (1,1), (0,0), (0,1), (1,2), (2,2)},
					(1,0):{(1,1), (1,2), (0,0), (2,0)},
					(1,1):{(0,0), (2,2), (2,0), (0,2), (1,0), (1,2), (0,1), (2,1)},
					(1,2):{(0,2), (2,2), (1,0), (1,1)},
					(2,0):{(1,1), (0,2), (2,1), (2,2), (0,0), (1,0)},
					(2,1):{(2,0), (2,2), (0,1), (1,1)},
					(2,2):{(0,0), (1,1), (2,0), (2,1), (0,2), (1,2)}}

	# Sets that indicate User is at the matchpoint
	matchpoint_sets = 	[{(0,0), (1,1)},
						{(0,0), (2,2)},
						{(1,1), (2,2)},
						{(2,0), (1,1)},
						{(2,0), (0,2)},
						{(1,1), (0,2)},
						{(0,0), (0,1)},
						{(0,0), (0,2)},
						{(0,1), (0,2)},
						{(1,0), (1,1)},
						{(1,0), (1,2)},
						{(1,2), (1,1)},
						{(2,0), (2,1)},
						{(2,0), (2,2)},
						{(2,2), (2,1)},
						{(0,0), (1,0)},
						{(0,0), (2,0)},
						{(1,0), (2,0)},
						{(0,1), (1,1)},
						{(0,1), (2,1)},
						{(2,1), (1,1)},
						{(0,2), (1,2)},
						{(0,2), (2,2)},
						{(2,2), (1,2)}]

	moves_available = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]


	computer_moves = []
	user_moves = []

	user_move_count = 0
	computer_move_count = 0

	update_screen(grid)
	next_move(user_moves, computer_moves, user_move_count, computer_move_count,
			grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
	


def update_screen(grid):
	for row in grid:
		print(*row)


def computer_init_move(moves_available):
	if (1,1) in moves_available: 
		return (1,1)
	else:
		x = randint(0, 2)
		y = randint(0, 2)
		return (x, y)


def raw_user_move():
	move = str(input("\nMake your move: \nSelect a box by typing its coordinates with number first and letter second, e.g. '1A'\n"))
	if len(move) != 2:
		print("\nYou must type exactly one letter and one number")
		raw_user_move()
	elif move[0] != "1" and move[0] != "2" and move[0] != "3":
		print("\nYou must type a number between 1 and 3 first")
		raw_user_move()
	elif move[1].lower() != "a" and move[1].lower() != "b" and move[1].lower() != "c":
		print("\nYou must type a letter between 'a' and 'c' second")
		raw_user_move()
	else:
		x = set_x(move)
		y = set_y(move)
		return (x, y)


def set_x(move):
	if "1" in move:
		return 0
	elif "2" in move:
		return 1
	elif "3" in move:
		return 2
	

def set_y(move):
	if "a" in move.lower():
		return 0
	elif "b" in move.lower():
		return 1
	elif "c" in move.lower():
		return 2


def next_move(user_moves, computer_moves, user_move_count, computer_move_count, grid, win_sets, 
			advantage_sets, matchpoint_sets, moves_available):
	if len(user_moves) == len(computer_moves):
		user_move(user_moves, computer_moves, user_move_count, computer_move_count,
				grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
	else:
		computer_move(user_moves, computer_moves, user_move_count, computer_move_count,
			grid, win_sets, advantage_sets, matchpoint_sets, moves_available)


def user_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
		grid):
	"""Checks for new coordinate values stored in user_moves 
		based off of the move_count and overwrites row values for X at selected
		coordinates.  """
	
	if user_moves:
		if user_moves[user_move_count][0] == 0:
			if user_moves[user_move_count][1] == 0:
				grid[1][2] = "X"
			elif user_moves[user_move_count][1] == 1:
				grid[3][2] = "X"
			elif user_moves[user_move_count][1] == 2:
				grid[5][2] = "X"
		elif user_moves[user_move_count][0] == 1:
			if user_moves[user_move_count][1] == 0:
				grid[1][4] = "X"
			elif user_moves[user_move_count][1] == 1:
				grid[3][4] = "X"
			elif user_moves[user_move_count][1] == 2:
				grid[5][4] = "X"
		elif user_moves[user_move_count][0] == 2:
			if user_moves[user_move_count][1] == 0:
				grid[1][6] = "X"
			elif user_moves[user_move_count][1] == 1:
				grid[3][6] = "X"
			elif user_moves[user_move_count][1] == 2:
				grid[5][6] = "X"


def computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
		grid):
	"""Checks for new coordinate values stored in computer_moves
		based off of the move_count and overwrites row values for O at selected
		coordinates.  """
	if computer_moves: 
		if computer_moves[computer_move_count][0] == 0:
			if computer_moves[computer_move_count][1] == 0:
				grid[1][2] = "O"
			elif computer_moves[computer_move_count][1] == 1:
				grid[3][2] = "O"
			elif computer_moves[computer_move_count][1] == 2:
				grid[5][2] = "O"
		elif computer_moves[computer_move_count][0] == 1:
			if computer_moves[computer_move_count][1] == 0:
				grid[1][4] = "O"
			elif computer_moves[computer_move_count][1] == 1:
				grid[3][4] = "O"
			elif computer_moves[computer_move_count][1] == 2:
				grid[5][4] = "O"
		elif computer_moves[computer_move_count][0] == 2:
			if computer_moves[computer_move_count][1] == 0:
				grid[1][6] = "O"
			elif computer_moves[computer_move_count][1] == 1:
				grid[3][6] = "O"
			elif computer_moves[computer_move_count][1] == 2:
				grid[5][6] = "O"

	
def evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
		grid, win_sets, advantage_sets, matchpoint_sets, moves_available):
	"""In this game there are three ways to win:  3 in a row down, across or diagonal.
	To evaluate a '3-in-a-row' downward, a specific x-value would need to appear in user_moves or 
	computer_moves (separately) exactly three times. Likewise, a 3 in a row across would be a y-value
	appearing 3 times. A diagonal win would only happen in two circumstances: 1.) [(0,0), (1,1), (2,2) or
	2.) [(2,0), (1,1), (0,2)]"""
	game_won = []

	for win_set in win_sets:
		if win_set.issubset(user_moves):
			game_won.append("You win!!")
		elif win_set.issubset(computer_moves):
			game_won.append("YOU LOSE!!")
	if game_won:
		print(game_won[0])
	else:
		if moves_available:
			next_move(user_moves, computer_moves, user_move_count, computer_move_count, 
				grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
		else: 
			print("STALEMATE. GAME OVER.")
			


def matchpoint_block(list_of_matchpoint_sets, win_sets):
	# Matchpoint sets (one step away from winning...computer will abandon smart_move() to block)
	matchpoint_block_sets = []

	for win_set in win_sets:
		for matchpoint_set in list_of_matchpoint_sets:
			if matchpoint_set.issubset(win_set):
				matchpoint_block_sets.append(win_set.difference(matchpoint_set))
	return matchpoint_block_sets 



def is_it_matchpoint(user_moves, matchpoint_sets):
	answers = []
	for group in matchpoint_sets:
		if group.issubset(user_moves):
			answers.append(group)
		else:
			pass
	if answers:
		return answers
	else:
		return False


def computer_move(user_moves, computer_moves, user_move_count, computer_move_count, grid, win_sets, 
			advantage_sets, matchpoint_sets, moves_available):
	if computer_move_count == 0:
		raw_move = computer_init_move(moves_available)
		
		print("Raw move:  ", raw_move)

		if raw_move in user_moves:
			
			print("Raw move already in user_moves, computer move resetting")

			next_move(user_moves, computer_moves, user_move_count, computer_move_count,
				grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
		else:
			computer_moves.append(raw_move)

			print("Computer moves:  ", computer_moves)

			moves_available.remove(raw_move)

			print("Moves available:  ", moves_available)

			computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
				grid)
			computer_move_count += 1
			
			sleep(3)
			update_screen(grid)
			evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
				grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
	elif is_it_matchpoint(user_moves, matchpoint_sets):

		print("IT IS MATCHPOINT")


		list_of_matchpoint_sets = is_it_matchpoint(user_moves, matchpoint_sets)

		print("list of Matchpoint sets:  ", list_of_matchpoint_sets)

		block_move_set_list = matchpoint_block(list_of_matchpoint_sets, win_sets)

		print("Block move set list:  ", block_move_set_list)




		

		unused_moves = []
		for block_move_set in block_move_set_list:
			
			
			block_move = block_move_set.pop()
			

			print("Block move:  ", block_move)


			if block_move in computer_moves:
				# pass
				print(block_move, "already in computer_moves")
				# print("FALSE ALARM:  It is not actually matchpoint")


				# raw_move = smart_move(computer_move_count, computer_moves, advantage_sets, moves_available)

				# print("Raw move (smart move):  ", smart_move)

				# computer_moves.append(raw_move)

				# print("Computer moves:  ", computer_moves)

				# moves_available.remove(raw_move)

				# print("Moves available:  ", moves_available)

				# computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
				# 	grid)
				# computer_move_count += 1
				
				# sleep(3)
				# update_screen(grid)
				# evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
				# 	grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
			else:
				unused_moves.append(block_move)
		if unused_moves:
			computer_moves.append(unused_moves[0])

			print("Computer moves:  ", computer_moves)

			moves_available.remove(unused_moves[0])

			print("Moves available:  ", moves_available)

			computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
				grid)
			computer_move_count += 1
			
			sleep(3)
			update_screen(grid)
			evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
				grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
		else: 
			raw_move = smart_move(computer_move_count, computer_moves, advantage_sets, moves_available)

			print("Raw smart move set:  ", raw_move_set)

			# raw_move = raw_move_set.pop()

			# print("Raw smart move:  ", raw_move)

			# if raw_move not in moves_available:
			# 	forced_move = forced_move(moves_available)
			# 	computer_moves.append(forced_move)
			# 	moves_available.remove(forced_move)
			# 	computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
			# 		grid)
			# 	computer_move_count += 1
				
			# 	sleep(3)
			# 	update_screen(grid)
			# 	evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
			# 		grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
			
			# else:
			computer_moves.append(raw_move)

			print("Computer moves:  ", computer_moves)

			moves_available.remove(raw_move)

			print("Moves available:  ", moves_available)

			computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
				grid)
			computer_move_count += 1
			
			sleep(3)
			update_screen(grid)
			evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
				grid, win_sets, advantage_sets, matchpoint_sets, moves_available)

	else:
		raw_move = smart_move(computer_move_count, computer_moves, advantage_sets, moves_available)


		print("Raw smart move:  ", raw_move)

		# if raw_move not in moves_available:
		# 	forced_move = forced_move(moves_available)
		# 	computer_moves.append(forced_move)
		# 	moves_available.remove(forced_move)
		# 	computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
		# 		grid)
		# 	computer_move_count += 1
			
		# 	sleep(3)
		# 	update_screen(grid)
		# 	evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
		# 		grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
		
		# else:
		computer_moves.append(raw_move)

		print("Computer moves:  ", computer_moves)

		moves_available.remove(raw_move)

		print("Moves available:  ", moves_available)

		computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
			grid)
		computer_move_count += 1
		
		sleep(3)
		update_screen(grid)
		evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
			grid, win_sets, advantage_sets, matchpoint_sets, moves_available)

	
def user_move(user_moves, computer_moves, user_move_count, computer_move_count,
			grid, win_sets, advantage_sets, matchpoint_sets, moves_available):
	raw_move = raw_user_move()
	if raw_move in user_moves:
		print("\nYou already played that square!")
		next_move(user_moves, computer_moves, user_move_count, computer_move_count,
			grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
	elif raw_move in computer_moves:
		print("\nThe computer already played that square! Try again")
		next_move(user_moves, computer_moves, user_move_count, computer_move_count,
			grid, win_sets, advantage_sets, matchpoint_sets, moves_available)
	else: 
		user_moves.append(raw_move)

		print("User moves:  ", user_moves)

		moves_available.remove(raw_move)

		print("Moves available:  ", moves_available)

		user_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
			grid)
		user_move_count += 1
		update_screen(grid)
		evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
			grid, win_sets, advantage_sets, matchpoint_sets, moves_available)




def smart_move(computer_move_count, computer_moves, advantage_sets, moves_available):
	usable_moves = []
	last_move = computer_moves[computer_move_count-1]
	
	for v in advantage_sets[last_move]:
		if v in moves_available:
			usable_moves.append(v)
	if usable_moves:

		print("Smart move--Usable moves:  ", usable_moves)

		return usable_moves[randint(0, len(usable_moves)-1)]
	else:
	
		print("No usable smart moves, calling forced move instead")

		return moves_available[randint(0, len(moves_available)-1)]
	


tic_tac_toe()


