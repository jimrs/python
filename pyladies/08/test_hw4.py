import pytest

import hw4

def test_setAlgebra():
    pets = ["pes", "kocka", "kralik", "had"]
    petss = ["pes", "ptak", "kocka", "sojka"]
    assert hw4.setAlgebra(pets, petss) == ( ["pes", "kocka", "kralik", "had", "ptak", "sojka"], 
                                            ["pes", "kocka"], 
                                            ["ptak", "sojka"])