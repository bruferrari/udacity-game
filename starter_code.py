#!/usr/bin/env python3

import random 

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self, move):
        return move

    def random_move(self):
        random.shuffle(moves)
        return moves[random.randint(0,len(moves)-1)]

    def evaluate(self, my_move, their_move):
        if beats(my_move, their_move):
            print("Player one wins!")
        elif my_move == their_move:
            print("Draw!")
        else:
            print("Player two wins!")

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_user_input(self):
        user_input = raw_input("Type (Rock, Paper or Scissors?)")
        print("Player 1 choose {}".format(user_input))
        return user_input

    def play_round(self):
        move = self.get_user_input()

        move1 = self.p1.move(move)
        move2 = self.p2.random_move()

        print("Player 1: {}  Player 2: {}".format(move1, move2))

        self.p1.evaluate(move1, move2)
    
    def play_game(self):
        print("Game start!")
        for round in range(3):
            print("Round {}:".format(round))
            self.play_round()
        print("Game over!")

if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
