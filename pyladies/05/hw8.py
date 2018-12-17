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

while player2 != 6:
    score2 += 1
    player2 = hod()
    print('Hrac 2 hodil ...', player2)

while player3 != 6:
    score3 += 1
    player3 = hod()
    print('Hrac 3 hodil ...', player3)

while player4 != 6:
    score4 += 1
    player4 = hod()
    print('Hrac 4 hodil ...', player4)

scores = [score1, score2, score3, score4]
win_score = min(scores)
win_player = scores.index(win_score) + 1    # list se indexuje od 0, proto je tam +1; funkce index vrati index prvniho vyskytu argumentu (coz je nejlepsi skore)

print('Vyhral hrac cislo', win_player, 'se skore', win_score, '(mene je lepsi).')