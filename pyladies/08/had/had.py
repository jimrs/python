def draw_field(coords):
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

	for coord in coords:
		field[coord[1] ][coord[0] ] = 'X'

	for row in range(len(field)):
		for col in range(len(field[row])):
			print(field[row][col], end='')

		print()


def move(coords, direction):
	lastCoord = coords[len(coords) - 1]

	if direction == 'n':
		newCoord = (lastCoord[0], lastCoord[1] - 1)
		coords.append(newCoord)
		coords.pop(0)

	elif direction == 's':
		newCoord = (lastCoord[0], lastCoord[1] + 1)
		coords.append(newCoord)
		coords.pop(0)

	elif direction == 'w':
		newCoord = (lastCoord[0] - 1, lastCoord[1])
		coords.append(newCoord)
		coords.pop(0)

	elif direction == 'e':
		newCoord = (lastCoord[0] + 1, lastCoord[1])
		coords.append(newCoord)
		coords.pop(0)

	else:
		raise ValueError('The provided direction is not valid (n, s, w, e).')

def game():
	coords = [(0, 0), (1, 0), (2, 0)]
	draw_field(coords)

	while True:
		userDirection = input("Enter your desired direction of travel (n, s, w, e), or enter q for quit: ")
		
		if userDirection != 'q':
			move(coords, userDirection)
			draw_field(coords)		
		else:
			break

#game()
