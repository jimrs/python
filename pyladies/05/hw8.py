from random import randrange

def hod():
    return randrange(1, 7)

score1 = 0
score2 = 0
score3 = 0
score4 = 0

player1 = 0
player2 = 0
player3 = 0
player4 = 0

while player1 != 6:
    score1 += 1
    player1 = hod()
    print('Hrac 1 hodil ...', player1)



