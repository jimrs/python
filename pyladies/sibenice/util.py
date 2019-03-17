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
    return ["bankovka"]

def guessInWord(word, guess):
    return guess in word

def guessInSecret(secret, guess):
    return guess in secret

def updateSecret(word, secret, guess):
    secretAsList = list(secret)
    index = 0

    for char in word:
        if char == guess and char not in secret:    # misto druhe podminky lze pouzit guessInSecret
            secretAsList[index] = guess
        index += 1

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

def isGuessValid(guess):
    if len(guess) > 1:
        return False
    else:
        return guess.isalpha()
