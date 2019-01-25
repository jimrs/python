import pytest

import util

def test_createWordList():
    expected = ["kokot"]
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

def test_guessInSecret():
    secret = "ji-k-"
    guess = "k"
    assert util.guessInSecret(secret, guess) == True

def test_updateSecret():
    word = "cobolo"
    guess = "o"
    secret = "c---l-"
    assert util.updateSecret(word, secret, guess) == "co-olo"

def test_noHyphenInSecret():
    secretBad = "jirka"
    secretGood = "ji-ka"
    assert util.noHyphenInSecret(secretBad) == True
    assert util.noHyphenInSecret(secretGood) == False

def test_isGuessValid():
    guess1 = "1"
    guess2 = "!"
    guess3 = "abc"
    guessGood = "a"
    assert util.isGuessValid(guess1) == False 
    assert util.isGuessValid(guess2) == False 
    assert util.isGuessValid(guess3) == False 
    assert util.isGuessValid(guessGood) == True