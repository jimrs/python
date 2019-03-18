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
