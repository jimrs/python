import random

def draw_field(coords, food):
	field = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],]

	for fruit in food:
		field[fruit[1] ][fruit[0] ] = '?'

	for coord in coords:
		field[coord[1] ][coord[0] ] = 'X'

	for row in range(len(field)):
		for col in range(len(field[row])):
			print(field[row][col], end='')

		print()


def move(coords, direction, food):
	lastCoord = coords[len(coords) - 1]

	if direction == 'w':	# north
		newCoord = (lastCoord[0], lastCoord[1] - 1)

	elif direction == 's':	# south
		newCoord = (lastCoord[0], lastCoord[1] + 1)

	elif direction == 'a':	# west
		newCoord = (lastCoord[0] - 1, lastCoord[1])		

	elif direction == 'd':	# east
		newCoord = (lastCoord[0] + 1, lastCoord[1])

	else:
		raise ValueError('The provided direction is not valid (wsad).')


	if newCoord in coords:
		raise ValueError('Game over. Stepped on your tail.')
	elif newCoord[0] > 9 or newCoord[0] < 0 or newCoord[1] > 9 or newCoord[1] < 0:
		raise ValueError('Game over. Stepped outside of bounds of the game field.') 
	else:
		coords.append(newCoord)
		if newCoord not in food:	# if the new coordinate doesnt have food on it, the tail will move (pop), because the snake didnt eat anything new
			coords.pop(0)			# if the new coordinate has food, the pop method will not be done, thus making the snake longer
		else:
			food.remove(newCoord)	# if the snake eats, food is removed at the position of newCoord

def game():
	coords = [(0, 0), (1, 0), (2, 0)]
	food = [(2, 3)]
	turn = 0
	draw_field(coords, food)

	while True:
		userDirection = input("Enter your desired direction of travel (wsad), or enter q for quit: ")
		
		if userDirection != 'q':
			turn += 1
			move(coords, userDirection, food)
			checkForFood(coords, food, turn)
			draw_field(coords, food)		
		else:
			break

def checkForFood(coords, food, turn):
	if food:	# if there is a fruit on the map
		if turn % 30 == 0:	# 30, 60, 90, 120...
			newFood(coords, food)

	else:
		newFood(coords, food)

def newFood(coords, food):
	while True:
		newFruit = (random.randrange(10), random.randrange(10))
		if newFruit in coords:
			continue
		else:
			food.append(newFruit)
			break

game()