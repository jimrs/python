import pytest

import hw8

def test_hasGoodFormat():
    good = "950920/1234"
    bad = "ab/cfd2"
    assert hw8.hasGoodFormat(good) is True
    assert hw8.hasGoodFormat(bad) is False

def test_isDivisibleBy11():
    good = "950920/1877"
    bad = "950920/1876"
    assert hw8.isDivisibleBy11(good) is True
    assert hw8.isDivisibleBy11(bad) is False

def test_dateOfBirth():
    bn = "950920/1877"
    assert hw8.dateOfBirth(bn) == (20, 9, 1995)

def test_gender():
    man = "950920/1877"
    woman = "955920/1871"
    assert hw8.gender(man) == "man"
    assert hw8.gender(woman) == "woman"
