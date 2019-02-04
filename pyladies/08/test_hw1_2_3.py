import pytest

import hw1_2_3

def test_stringShorterThanFive():
    pets = ["pes", "kocka", "kralik", "had"]
    assert hw1_2_3.stringShorterThanFive(pets) == ["pes", "had"]

def test_stringBeginningWithK():
    pets = ["pes", "kocka", "kralik", "had"]
    assert hw1_2_3.stringBeginningWithK(pets) == ["kocka", "kralik"]