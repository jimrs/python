import util
import sys

while True:     # new game loop

    wordList = util.createWordList()
    word = util.pickWord(wordList)
    secret = util.createSecret(word)
    badGuessCount = 0
    newGame = False

    while True: # game round loop
        guess = input("INPUT GUESS: ")

        if util.isGuessValid(guess):
            if util.guessInSecret(secret, guess):
                badGuessCount += 1
                print("GUESS ALREADY GUESSED.")

            elif util.guessInWord(word, guess):
                secret = util.updateSecret(word, secret, guess)

            else:
                badGuessCount += 1
                print("GUESS BAD.")

            util.printSecret(secret)

            if util.noHyphenInSecret(secret):
                print("YOU HAVE WON.")
                
                while True:
                        answer = input("PLAY AGAIN? Y/N ")
                        if answer == "Y":
                            newGame = True
                            break
                        elif answer == "N":
                            sys.exit()
                        else:
                            print("WRONG.")
            else:
                util.printGameStatus(badGuessCount)
                if badGuessCount >= 9:
                    print("GAME LOST.")
                    
                    while True:
                        answer = input("PLAY AGAIN? Y/N ")
                        if answer == "Y":
                            newGame = True
                            break
                        elif answer == "N":
                            sys.exit()
                        else:
                            print("WRONG.")

        else:
            print("INVALID GUESS. TRY AGAIN.")

        if newGame is True:
            break

