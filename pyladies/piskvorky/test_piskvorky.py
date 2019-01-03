import pytest

import piskvorky
import ai
import util

# ai testy
def test_tah_na_prazdne_pole():
    pole = ai.tah_pocitace('--------------------')
    assert len(pole) == 20
    assert pole.count('o') == 1
    assert pole.count('-') == 19

def test_tah_na_plne_pole():
	with pytest.raises(Exception):
		pole = ai.tah_pocitace('xxxxxxxxxxxxxxxxxxxx')

def test_null_pole():
    with pytest.raises(TypeError):
        pole = ai.tah_pocitace(None)