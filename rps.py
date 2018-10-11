#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.score = 0

    def move(self, move):
        return move

    def play(self):
        return moves[0]

    def evaluate(self, my_move, their_move):
        if beats(my_move, their_move):
            print("Player one wins!")
        elif my_move == their_move:
            print("Draw!")
        else:
            print("Player two wins!")


class RandomPlayer(Player):
    def play(self):
        random.shuffle(moves)
        return moves[random.randint(0, len(moves)-1)]


class ReflectionPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def play(self):
        if self.their_move is None:
            return moves[random.randint(0, len(moves)-1)]
        return self.their_move

    def learn(self, their_move):
        self.their_move = their_move


class HumanPlayer(Player):
    def get_user_input(self):
        user_input = raw_input("Type (Rock, Paper or Scissors?)")
        print("Player 1 choose {}".format(user_input))
        return user_input

    def play(self):
        player_move = self.get_user_input()
        while player_move not in moves:
            player_move = self.get_user_input()
            print("Option not recognized, play again...")
        return player_move


class AlternativePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def play(self):
        move = None
        if self.their_move is None:
            move = Player.play(self)
        else:
            index = moves.index(self.their_move) + 1
            if index >= len(moves):
                index = 0

            move = moves[index]
        self.their_move = move
        return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):

        move1 = self.p1.play()
        index = random.randint(0, len(self.p2)-1)
        move2 = self.p2[index].play()

        print("Player 1: {}  Player 2: {}".format(move1, move2))

        self.p1.evaluate(move1, move2)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print("Round {}:".format(round + 1))
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), [RandomPlayer(), ReflectionPlayer(),
                Player(), AlternativePlayer()])
    game.play_game()
