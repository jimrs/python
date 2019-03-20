import had

import pytest

def test_moveAndEat():
	souradnice = [(0, 0)]
	food = [(2, 3)]
	had.move(souradnice, 'd', food )
	assert souradnice == [(1, 0)]
	had.move(souradnice, 'd', food )
	assert souradnice == [(2, 0)]
	had.move(souradnice, 's', food )
	assert souradnice == [(2, 1)]
	had.move(souradnice, 'w', food )
	assert souradnice == [(2, 0)]

	with pytest.raises(ValueError):
		had.move(souradnice, 'g', food )

	souradnice = [(0, 0), (1, 0), (2, 0)]
	with pytest.raises(ValueError):
		had.move(souradnice, 'w', food )	# out of bounds
	with pytest.raises(ValueError):
		had.move(souradnice, 'a', food )	# step on tail

	souradnice = [(9, 7), (9, 8), (9, 9)]
	with pytest.raises(ValueError):
		had.move(souradnice, 's', food )	# oob
	with pytest.raises(ValueError):
		had.move(souradnice, 'd', food )	# oob
	with pytest.raises(ValueError):
		had.move(souradnice, 'w', food )	# step on tail

	souradnice = [(2, 0), (2, 1), (2, 2)]
	had.move(souradnice, 's', food )		# move to eat
	assert len(souradnice) == 4

def test_checkForFood():
	souradnice = [(2, 0), (2, 1), (2, 2)]
	food = [(2, 3)]
	had.checkForFood(souradnice, food, 30)	# turn 30 means generate new food
	assert len(food) == 2
	had.move(souradnice, 's', food )		# move to eat
	assert len(food) == 1					# ate 1 fruit, 1 remains
	food = []
	assert len(food) == 0
	had.checkForFood(souradnice, food, 20)	# no food on the map means generate new food
	assert len(food) == 1

def test_newFood():
	food = []
	coords = [(0, 0), (1, 0), (2, 0)]
	had.newFood(coords, food)
	assert food 