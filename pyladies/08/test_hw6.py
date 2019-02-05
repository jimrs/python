import pytest

import hw6

def test_sortListBySecondChar():
    pets = ["pes","andulka","had","kočka","králík"]
    assert hw6.sortListBySecondChar(pets) == ["had","pes","andulka","kočka","králík"]