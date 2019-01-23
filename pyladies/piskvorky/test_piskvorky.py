import pytest

import piskvorky
import ai
import util

# ai testy
def test_ai_prazdne_pole():
    pole = ai.tah_pocitace('--------------------', 'o')
    assert len(pole) == 20
    assert pole.count('o') == 1
    assert pole.count('-') == 19

def test_ai_plne_pole():
    with pytest.raises(Exception):
            pole = ai.tah_pocitace('xxxxxxxxxxxxxxxxxxxx', 'o')

def test_ai_null_pole():
    with pytest.raises(TypeError):
        pole = ai.tah_pocitace(None, None)

def test_ai_delsi_pole():
    pole = ai.tah_pocitace('---------------------', 'o') # delka 21
    assert len(pole) == 21
    assert pole.count('o') == 1
    assert pole.count('-') == 20

# util testy
def test_tah_mimo_rozsah():
    with pytest.raises(IndexError):
        plan = '--------------------'
        pole = util.tah(plan, 100, 'o')

def test_tah_null_symbol():
    with pytest.raises(Exception):
        plan = '--------------------'
        pole = util.tah(plan, 10, None)

def test_vyhodnot_null():
    with pytest.raises(Exception):
        util.vyhodnot(None)

def test_vyhodnot_spatne_pole():
    pole = "kocicka"
    assert util.vyhodnot(pole) == "!"   # vrati "remizu"

def test_user_input_pismeno():
    plan = '--------------------'
    assert util.isUserPositionValid(plan, 'a') is False

def test_user_input_mimo_rozsah():
    plan = '--------------------'
    assert util.isUserPositionValid(plan, 300) is False