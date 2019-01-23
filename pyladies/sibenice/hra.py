import util

wordList = util.createWordList()
word = util.pickWord(wordList)
secret = util.createSecret(word)
badGuessCount = 0

while True:
    guess = input("INPUT GUESS: ")

    if util.guessInWord(word, guess):
        secret = util.updateSecret(word, secret, guess)
    else:
        badGuessCount += 1
        print("GUESS BAD.")

    util.printSecret(secret)

    if util.noHyphenInSecret(secret):
        print("YOU HAVE WON.")
        break
    else:
        util.printGameStatus(badGuessCount)
        if badGuessCount >= 9:
            print("GAME LOST.")
            break


