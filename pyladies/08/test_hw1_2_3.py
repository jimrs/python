import pytest

import hw1_2_3

def test_stringShorterThanFive():
    pets = ["pes", "kocka", "kralik", "had"]
    assert hw1_2_3.stringShorterThanFive(pets) == ["pes", "had"]

def test_stringBeginningWithK():
    pets = ["pes", "kocka", "kralik", "had"]
    assert hw1_2_3.stringBeginningWithK(pets) == ["kocka", "kralik"]

def test_isStringInList():
    pets = ["pes", "kocka", "kralik", "had"]
    assert hw1_2_3.isStringInList("had", pets) is True
    assert hw1_2_3.isStringInList("benis", pets) is False