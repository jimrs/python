import hw9

import pytest

def test_romanToInt():
	romans = ["I", "II", "III", "IV", "V",
	"VI", "VII", "VIII", "IX", "X",
	"XI", "XII", "XIII", "XIV", "XV",
	"XVI", "XVII", "XVIII", "XIX", "XX"]

	for i in range(len(romans)):
		assert hw9.romanToInt(romans[i]) == (i+1)