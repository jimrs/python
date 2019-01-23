import pytest

import util

def test_createWordList():
    expected = ["jirka", "francie", "sunka"]
    assert util.createWordList() == expected

def test_pickWord():
    wordList = ["jirka", "francie", "sunka"]
    word = util.pickWord(wordList)
    assert (word in wordList) == True

def test_createSecret():
    word = "jirka"
    expected = "-----"  # 5 underscores for 5 chars
    assert util.createSecret(word) == expected

def test_guessInWord():
    word = "jirka"
    guess = "k"
    assert util.guessInWord(word, guess) == True

def test_updateSecret():
    word = "jirka"
    guess = "k"
    secret = "-----"
    assert util.updateSecret(word, secret, guess) == "---k-"

def test_noHyphenInSecret():
    secret = "jirka"
    assert util.noHyphenInSecret(secret) == True

