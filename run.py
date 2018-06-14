#!/usr/bin/env python

# URL: https://www.reddit.com/r/math/comments/3eytm1/nontransitive_dice_an_rmath_conpetition/

import os


players = [
    [10, 10, 10, 10, 10, 10],
    [-10, -10, -10, -10, 0, 100],
]


def my_random(n):
    rand = 0
    for ch in os.urandom(n):
        rand += ord(ch)
    return rand % n

def random_pick_one(player):
    return player[my_random(6)]


def verify_player(player):
    if sum(player) != 60:
        raise Exception("Player %s not = 60" % get_player(player))
    if not all(map(lambda x: -10 <= x and x <= 100, player)):
        raise Exception("Player %s out of range [-10, 100]" % get_player(player))


def run_once(player1, player2):
    n1 = 0
    n2 = 0
    while n1 < 100 and n2 < 100:
        p1 = random_pick_one(player1)
        p2 = random_pick_one(player2)
        if p1 > p2:
            n1 += p1 - p2
        elif p2 > p1:
            n2 += p2 - p1
    if n1 >= 100:
        return 1
    elif n2 >= 100:
        return 2
    else:
        raise Exception("Error state")


def run_n_times(player1, player2, n):
    win1 = 0
    win2 = 0
    for i in range(n):
        win = run_once(players[0], players[1])
        if win == 1:
            win1 += 1
        elif win == 2:
            win2 += 1
    return win1, win2

verify_player(players[0])
verify_player(players[1])


def battle(player1, player2):
    n = 1000
    win1, win2 = run_n_times(player1, player2, n)
    print get_player(player1), ',', get_player(player2)
    print win1, ',', win2, '/', n


def get_player(player):
    return repr(player)


def random_player():
    n = set()
    while len(n) != 6:
        n = set([
            my_random(101) - 40,
            my_random(101) - 40,
            my_random(101) - 40,
            my_random(101) - 40,
            my_random(101) - 40,
            my_random(101) - 40,
        ])
    n = sorted(n)
    


battle(players[0], players[1])

battle(
    [10, 10, 10, 10, 10, 10],
    [8,9,10,11,12,12],
)



