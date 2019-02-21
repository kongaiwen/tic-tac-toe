from random import randint
from time import sleep

def tic_tac_toe():
	row_0 = [" ", ".__1___.___2__.___3__."]
	row_1 = [" ", "|  ", " ", " |  ", " ", " |  ", " ", " |"]
	row_2 = ["A", "|______|______|______|"]
	row_3 = [" ", "|  ", " ", " |  ", " ", " |  ", " ", " |"]
	row_4 = ["B", "|______|______|______|"]
	row_5 = [" ", "|  ", " ", " |  ", " ", " |  ", " ", " |"]
	row_6 = ["C", "|______|______|______|"]

	
	# Winning Sets
	win_1 = [(0,0), (1,1), (2,2)]
	win_2 = [(2,0), (1,1), (0,2)]
	win_3 = [(0,0), (0,1), (0,2)]
	win_4 = [(1,0), (1,1), (1,2)]
	win_5 = [(2,0), (2,1), (2,2)]
	win_6 = [(0,0), (1,0), (2,0)]
	win_7 = [(0,1), (1,1), (2,1)]
	win_8 = [(0,2), (1,2), (2,2)]



	# Winning coordinate pathways sets
	zero_0 = [(1,1), (2,2), (0,1), (0,2), (1,0), (2,0)]
	zero_1 = [(0,0), (0,2), (1,1), (2,1)]
	zero_2 = [(2,0), (1,1), (0,0), (0,1), (1,2), (2,2)]
	one_0 = [(1,1), (1,2), (0,0), (2,0)]
	one_1 = [(0,0), (2,2), (2,0), (0,2), (1,0), (1,2), (0,1), (2,1)]
	one_2 = [(0,2), (2,2), (1,0), (1,1)]
	two_0 = [(1,1), (0,2), (2,1), (2,2), (0,0), (1,0)]
	two_1 = [(2,0), (2,2), (0,1), (1,1)]
	two_2 = [(0,0), (1,1), (2,0), (2,1), (0,2), (1,2)]

	computer_moves = []
	user_moves = []

	user_move_count = 0
	computer_move_count = 0

	update_screen(row_0, row_1, row_2, row_3, row_4, row_5, row_6)
	next_move(user_moves, computer_moves, user_move_count, computer_move_count,
			row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, 
			win_4, win_5, win_6, win_7, win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2,
			two_0, two_1, two_2)
	


def update_screen(row_0, row_1, row_2, row_3, row_4, row_5, row_6):
	print(*row_0)
	print(*row_1)
	print(*row_2)
	print(*row_3)
	print(*row_4)
	print(*row_5)
	print(*row_6)


def computer_init_move():
	x = randint(0, 2)
	y = randint(0, 2)
	return (x, y)
	# print((x, y))

def user_move():
	move = str(input("\nMake your move: \nSelect a box by typing its coordinates with number first and letter second, e.g. '1A'\n"))
	if len(move) != 2:
		print("\nYou must type exactly one letter and one number")
		user_move()
	elif move[0] != "1" and move[0] != "2" and move[0] != "3":
		print("\nYou must type a number between 1 and 3 first")
		user_move()
	elif move[1].lower() != "a" and move[1].lower() != "b" and move[1].lower() != "c":
		print("\nYou must type a letter between 'a' and 'c' second")
		user_move()
	else:
		x = set_x(move)
		y = set_y(move)
		return (x, y)
		# print(x, y)


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


def next_move(user_moves, computer_moves, user_move_count, computer_move_count, row_0, row_1,
			row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, win_5, win_6, win_7, 
			win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2):
	if len(user_moves) == len(computer_moves):
		raw_move = user_move()
		if raw_move in user_moves:
			print("\nYou already played that square!")
			next_move(user_moves, computer_moves, user_move_count, computer_move_count,
				row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, win_5, win_6, win_7, 
				win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2)
		elif raw_move in computer_moves:
			print("\nThe computer already played that square! Try again")
			next_move(user_moves, computer_moves, user_move_count, computer_move_count,
				row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, win_5, win_6, win_7, 
				win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2)
		else: 
			user_moves.append(raw_move)
			user_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
				row_0, row_1, row_2, row_3, row_4, row_5, row_6)
			user_move_count += 1
			update_screen(row_0, row_1, row_2, row_3, row_4, row_5, row_6)
			evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
				row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4,
				win_5, win_6, win_7, win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, 
				two_1, two_2)
	else:
		if computer_move_count >= 1 and computer_move_count <= 3:
			strategize_next_move(user_moves, computer_moves, user_move_count, computer_move_count,
								row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, 
								win_4, win_5, win_6, win_7, win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2,
								two_0, two_1, two_2)
		elif computer_move_count > 3:
			raw_move = smart_move(computer_move_count, computer_moves, zero_0, zero_1, zero_2,
						one_0, one_1, one_2, two_0, two_1, two_2)
			if raw_move in computer_moves:
				next_move(user_moves, computer_moves, user_move_count, computer_move_count,
					row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, win_5, win_6, win_7, 
					win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2)
			elif raw_move in user_moves:
				next_move(user_moves, computer_moves, user_move_count, computer_move_count,
					row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, win_5, win_6, win_7, 
					win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2)
			else:
				computer_moves.append(raw_move)
				computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
					row_0, row_1, row_2, row_3, row_4, row_5, row_6)
				computer_move_count += 1
				
				sleep(3)
				update_screen(row_0, row_1, row_2, row_3, row_4, row_5, row_6)
				evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
					row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4,
					win_5, win_6, win_7, win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, 
					two_0, two_1, two_2)

		else:
			raw_move = computer_init_move()
			if raw_move in user_moves:
				next_move(user_moves, computer_moves, user_move_count, computer_move_count,
					row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, win_5, win_6, win_7, 
					win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2)
			else:
				computer_moves.append(raw_move)
				computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
					row_0, row_1, row_2, row_3, row_4, row_5, row_6)
				computer_move_count += 1
				
				sleep(3)
				update_screen(row_0, row_1, row_2, row_3, row_4, row_5, row_6)
				evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
					row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4,
					win_5, win_6, win_7, win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, 
					two_0, two_1, two_2)


def user_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
		row_0, row_1, row_2, row_3, row_4, row_5, row_6):
	"""Checks for new coordinate values stored in user_moves 
		based off of the move_count and overwrites row values for X at selected
		coordinates.  """
	
	if user_moves:
		if user_moves[user_move_count][0] == 0:
			if user_moves[user_move_count][1] == 0:
				row_1[2] = "X"
			elif user_moves[user_move_count][1] == 1:
				row_3[2] = "X"
			elif user_moves[user_move_count][1] == 2:
				row_5[2] = "X"
		elif user_moves[user_move_count][0] == 1:
			if user_moves[user_move_count][1] == 0:
				row_1[4] = "X"
			elif user_moves[user_move_count][1] == 1:
				row_3[4] = "X"
			elif user_moves[user_move_count][1] == 2:
				row_5[4] = "X"
		elif user_moves[user_move_count][0] == 2:
			if user_moves[user_move_count][1] == 0:
				row_1[6] = "X"
			elif user_moves[user_move_count][1] == 1:
				row_3[6] = "X"
			elif user_moves[user_move_count][1] == 2:
				row_5[6] = "X"


def computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
		row_0, row_1, row_2, row_3, row_4, row_5, row_6):
	"""Checks for new coordinate values stored in computer_moves
		based off of the move_count and overwrites row values for O at selected
		coordinates.  """
	if computer_moves: 
		if computer_moves[computer_move_count][0] == 0:
			if computer_moves[computer_move_count][1] == 0:
				row_1[2] = "O"
			elif computer_moves[computer_move_count][1] == 1:
				row_3[2] = "O"
			elif computer_moves[computer_move_count][1] == 2:
				row_5[2] = "O"
		elif computer_moves[computer_move_count][0] == 1:
			if computer_moves[computer_move_count][1] == 0:
				row_1[4] = "O"
			elif computer_moves[computer_move_count][1] == 1:
				row_3[4] = "O"
			elif computer_moves[computer_move_count][1] == 2:
				row_5[4] = "O"
		elif computer_moves[computer_move_count][0] == 2:
			if computer_moves[computer_move_count][1] == 0:
				row_1[6] = "O"
			elif computer_moves[computer_move_count][1] == 1:
				row_3[6] = "O"
			elif computer_moves[computer_move_count][1] == 2:
				row_5[6] = "O"

	
def evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
		row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, 
		win_5, win_6, win_7, win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2):
	"""In this game there are three ways to win:  3 in a row down, across or diagonal.
	To evaluate a '3-in-a-row' downward, a specific x-value would need to appear in user_moves or 
	computer_moves (separately) exactly three times. Likewise, a 3 in a row across would be a y-value
	appearing 3 times. A diagonal win would only happen in two circumstances: 1.) [(0,0), (1,1), (2,2) or
	2.) [(2,0), (1,1), (0,2)]"""
	if set(win_1).issubset(user_moves):
		print("\nYou win!")
	elif set(win_2).issubset(user_moves):
		print("\nYou win!")
	elif set(win_3).issubset(user_moves):
		print("\nYou win!")
	elif set(win_4).issubset(user_moves):
		print("\nYou win!")
	elif set(win_5).issubset(user_moves):
		print("\nYou win!")
	elif set(win_6).issubset(user_moves):
		print("\nYou win!")
	elif set(win_7).issubset(user_moves):
		print("\nYou win!")
	elif set(win_8).issubset(user_moves):
		print("\nYou win!")
	elif set(win_1).issubset(computer_moves):
		print("\nYou lose!")
	elif set(win_2).issubset(computer_moves):
		print("\nYou lose!")
	elif set(win_3).issubset(computer_moves):
		print("\nYou lose!")
	elif set(win_4).issubset(computer_moves):
		print("\nYou lose!")
	elif set(win_5).issubset(computer_moves):
		print("\nYou lose!")
	elif set(win_6).issubset(computer_moves):
		print("\nYou lose!")
	elif set(win_7).issubset(computer_moves):
		print("\nYou lose!")
	elif set(win_8).issubset(computer_moves):
		print("\nYou lose!")
	else:
		next_move(user_moves, computer_moves, user_move_count, computer_move_count, 
		row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, win_5,
		win_6, win_7, win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2)


def smart_move(computer_move_count, computer_moves, zero_0, zero_1, zero_2,
			one_0, one_1, one_2, two_0, two_1, two_2):
	if computer_move_count >= 1:
		if computer_moves[computer_move_count-1] == (0,0):
			return zero_0[randint(0, len(zero_0)-1)]
		elif computer_moves[computer_move_count-1] == (0,1):
			return zero_1[randint(0, len(zero_1)-1)]
		elif computer_moves[computer_move_count-1] == (0,2):
			return zero_2[randint(0, len(zero_2)-1)]
		elif computer_moves[computer_move_count-1] == (1,0):
			return one_0[randint(0, len(one_0)-1)]
		elif computer_moves[computer_move_count-1] == (1,1):
			return one_1[randint(0, len(one_1)-1)]
		elif computer_moves[computer_move_count-1] == (1,2):
			return one_2[randint(0, len(one_2)-1)]
		elif computer_moves[computer_move_count-1] == (2,0):
			return two_0[randint(0, len(two_0)-1)]
		elif computer_moves[computer_move_count-1] == (2,1):
			return two_1[randint(0, len(two_1)-1)]
		elif computer_moves[computer_move_count-1] == (2,2):
			return two_2[randint(0, len(two_2)-1)]


def matchpoint_block(user_moves):

	# Matchpoint sets (one step away from winning...computer will abandon smart_move() to block)
	
	match_1 = [(0,0), (1,1)] #(2,2)
	match_2 = [(0,0), (2,2)] #(1,1)
	match_3 = [(1,1), (2,2)] #(0,0)
	match_4 = [(2,0), (1,1)] #(0,2)
	match_5 = [(2,0), (0,2)] #(1,1)
	match_6 = [(1,1), (0,2)] #(2,0)
	match_7 = [(0,0), (0,1)] #(0,2)
	match_8 = [(0,0), (0,2)] #(0,1)
	match_9 = [(0,1), (0,2)] #(0,0)
	match_10 = [(1,0), (1,1)] #(1,2)
	match_11 = [(1,0), (1,2)] #(1,1)
	match_12 = [(1,2), (1,1)] #(1,0)
	match_13 = [(2,0), (2,1)] #(2,2)
	match_14 = [(2,0), (2,2)] #(2,1)
	match_15 = [(2,2), (2,1)] #(2,0)
	match_16 = [(0,0), (1,0)] #(2,0)
	match_17 = [(0,0), (2,0)] #(1,0)
	match_18 = [(1,0), (2,0)] #(0,0)
	match_19 = [(0,1), (1,1)] #(2,1)
	match_20 = [(0,1), (2,1)] #(1,1)
	match_21 = [(2,1), (1,1)] #(0,1)
	match_22 = [(0,2), (1,2)] #(2,2)
	match_23 = [(0,2), (2,2)] #(1,2)
	match_24 = [(2,2), (1,2)] #(0,2)

	if set(match_1).issubset(user_moves):
		return (2,2)
	elif set(match_13).issubset(user_moves):
		return (2,2)
	elif set(match_22).issubset(user_moves):
		return (2,2)
	elif set(match_2).issubset(user_moves):
		return (1,1)
	elif set(match_5).issubset(user_moves):
		return (1,1)
	elif set(match_11).issubset(user_moves):
		return (1,1)
	elif set(match_20).issubset(user_moves):
		return (1,1)
	elif set(match_3).issubset(user_moves):
		return (0,0)
	elif set(match_9).issubset(user_moves):
		return (0,0)
	elif set(match_18).issubset(user_moves):
		return (0,0)
	elif set(match_4).issubset(user_moves):
		return (0,2)
	elif set(match_7).issubset(user_moves):
		return (0,2)
	elif set(match_24).issubset(user_moves):
		return (0,2)
	elif set(match_6).issubset(user_moves):
		return (2,0)
	elif set(match_15).issubset(user_moves):
		return (2,0)
	elif set(match_16).issubset(user_moves):
		return (2,0)
	elif set(match_8).issubset(user_moves):
		return (0,1)
	elif set(match_21).issubset(user_moves):
		return (0,1)
	elif set(match_10).issubset(user_moves):
		return (1,2)
	elif set(match_23).issubset(user_moves):
		return (1,2)
	elif set(match_12).issubset(user_moves):
		return (1,0)
	elif set(match_17).issubset(user_moves):
		return (1,0)
	elif set(match_14).issubset(user_moves):
		return (2,1)
	elif set(match_19).issubset(user_moves):
		return (2,1)


def strategize_next_move(user_moves, computer_moves, user_move_count, computer_move_count,
			row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, 
			win_4, win_5, win_6, win_7, win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2,
			two_0, two_1, two_2):
	if is_it_matchpoint(user_moves):
		block_move = matchpoint_block(user_moves)
		if block_move in computer_moves:
			next_move(user_moves, computer_moves, user_move_count, computer_move_count,
				row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, win_5, win_6, win_7, 
				win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2)
		else:
			computer_moves.append(block_move)
			computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
				row_0, row_1, row_2, row_3, row_4, row_5, row_6)
			computer_move_count += 1
			
			sleep(3)
			update_screen(row_0, row_1, row_2, row_3, row_4, row_5, row_6)
			evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
				row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4,
				win_5, win_6, win_7, win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, 
				two_0, two_1, two_2)
	else:
		raw_move = smart_move(computer_move_count, computer_moves, zero_0, zero_1, zero_2,
						one_0, one_1, one_2, two_0, two_1, two_2)
		if raw_move in computer_moves:
			next_move(user_moves, computer_moves, user_move_count, computer_move_count,
				row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, win_5, win_6, win_7, 
				win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2)
		elif raw_move in user_moves:
			next_move(user_moves, computer_moves, user_move_count, computer_move_count,
				row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4, win_5, win_6, win_7, 
				win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, two_0, two_1, two_2)
		else:
			computer_moves.append(raw_move)
			computer_mark(user_moves, computer_moves, user_move_count, computer_move_count, 
				row_0, row_1, row_2, row_3, row_4, row_5, row_6)
			computer_move_count += 1
			
			sleep(3)
			update_screen(row_0, row_1, row_2, row_3, row_4, row_5, row_6)
			evaluate_board(user_moves, computer_moves, user_move_count, computer_move_count, 
				row_0, row_1, row_2, row_3, row_4, row_5, row_6, win_1, win_2, win_3, win_4,
				win_5, win_6, win_7, win_8, zero_0, zero_1, zero_2, one_0, one_1, one_2, 
				two_0, two_1, two_2)




def is_it_matchpoint(user_moves):
	match_1 = [(0,0), (1,1)] #(2,2)
	match_2 = [(0,0), (2,2)] #(1,1)
	match_3 = [(1,1), (2,2)] #(0,0)
	match_4 = [(2,0), (1,1)] #(0,2)
	match_5 = [(2,0), (0,2)] #(1,1)
	match_6 = [(1,1), (0,2)] #(2,0)
	match_7 = [(0,0), (0,1)] #(0,2)
	match_8 = [(0,0), (0,2)] #(0,1)
	match_9 = [(0,1), (0,2)] #(0,0)
	match_10 = [(1,0), (1,1)] #(1,2)
	match_11 = [(1,0), (1,2)] #(1,1)
	match_12 = [(1,2), (1,1)] #(1,0)
	match_13 = [(2,0), (2,1)] #(2,2)
	match_14 = [(2,0), (2,2)] #(2,1)
	match_15 = [(2,2), (2,1)] #(2,0)
	match_16 = [(0,0), (1,0)] #(2,0)
	match_17 = [(0,0), (2,0)] #(1,0)
	match_18 = [(1,0), (2,0)] #(0,0)
	match_19 = [(0,1), (1,1)] #(2,1)
	match_20 = [(0,1), (2,1)] #(1,1)
	match_21 = [(2,1), (1,1)] #(0,1)
	match_22 = [(0,2), (1,2)] #(2,2)
	match_23 = [(0,2), (2,2)] #(1,2)
	match_24 = [(2,2), (1,2)] #(0,2)

	if set(match_1).issubset(user_moves):
		return True
	elif set(match_13).issubset(user_moves):
		return True
	elif set(match_22).issubset(user_moves):
		return True
	elif set(match_2).issubset(user_moves):
		return True
	elif set(match_5).issubset(user_moves): 
		return True
	elif set(match_11).issubset(user_moves):
		return True
	elif set(match_20).issubset(user_moves):
		return True
	elif set(match_3).issubset(user_moves):
		return True
	elif set(match_9).issubset(user_moves): 
		return True
	elif set(match_18).issubset(user_moves):
		return True
	elif set(match_4).issubset(user_moves):
		return True
	elif set(match_7).issubset(user_moves): 
		return True
	elif set(match_24).issubset(user_moves):
		return True
	elif set(match_6).issubset(user_moves): 
		return True
	elif set(match_15).issubset(user_moves): 
		return True
	elif set(match_16).issubset(user_moves):
		return True
	elif set(match_8).issubset(user_moves):
		return True
	elif set(match_21).issubset(user_moves):
		return True
	elif set(match_10).issubset(user_moves):
		return True
	elif set(match_23).issubset(user_moves):
		return True
	elif set(match_12).issubset(user_moves): 
		return True
	elif set(match_17).issubset(user_moves):
		return True
	elif set(match_14).issubset(user_moves): 
		return True
	elif set(match_19).issubset(user_moves):
		return True
	else:
		return False







tic_tac_toe()


