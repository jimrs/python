from random import choice
import pic

def pickWord(wordList):
    return choice(wordList)

def createSecret(word):
    secret = ""
    for char in word:
        secret += "-"
    
    return secret

def createWordList():
    return ["jirka", "francie", "sunka"]

def guessInWord(word, guess):
    return guess in word

def updateSecret(word, secret, guess):
    index = word.index(guess)
    secretAsList = list(secret)
    secretAsList[index] = guess
    return "".join(secretAsList)

def printSecret(secret):
    print(secret)

def noHyphenInSecret(secret):
    return "-" not in secret    # pokud neni - v secret, TRUE

def printGameStatus(badGuessCount):
    statusList = [
        pic.zero, 
        pic.one, 
        pic.two, 
        pic.three, 
        pic.four, 
        pic.five, 
        pic.six, 
        pic.seven, 
        pic.eight, 
        pic.nine
    ]

    print(statusList[badGuessCount])