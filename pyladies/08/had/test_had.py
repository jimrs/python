import had

import pytest

def test_move():
	souradnice = [(0, 0)]
	had.move(souradnice, 'e')
	assert souradnice == [(1, 0)]
	had.move(souradnice, 'e')
	assert souradnice == [(2, 0)]
	had.move(souradnice, 's')
	assert souradnice == [(2, 1)]
	had.move(souradnice, 'n')
	assert souradnice == [(2, 0)]

	with pytest.raises(ValueError):
		had.move(souradnice, 'g')

	souradnice = [(0, 0), (1, 0), (2, 0)]
	with pytest.raises(ValueError):
		had.move(souradnice, 'n')	# out of bounds
	with pytest.raises(ValueError):
		had.move(souradnice, 'w')	# step on tail

	souradnice = [(9, 7), (9, 8), (9, 9)]
	with pytest.raises(ValueError):
		had.move(souradnice, 's')	# oob
	with pytest.raises(ValueError):
		had.move(souradnice, 'e')	# oob
	with pytest.raises(ValueError):
		had.move(souradnice, 'n')	# step on tail