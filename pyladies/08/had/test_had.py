import had

import pytest

def test_move():
	souradnice = [(0, 0)]
	had.move(souradnice, 'e')
	assert souradnice == [(0, 0), (1, 0)]
	had.move(souradnice, 'e')
	assert souradnice == [(0, 0), (1, 0), (2, 0)]
	had.move(souradnice, 's')
	assert souradnice == [(0, 0), (1, 0), (2, 0), (2, 1)]
	had.move(souradnice, 'n')
	assert souradnice == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]

	with pytest.raises(ValueError):
		had.move(souradnice, 'g')
