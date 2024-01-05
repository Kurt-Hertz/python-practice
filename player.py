import math
import random

class Player:
    def __init__(self, letter):
        # x and o
        self.letter = letter

    def get_move(self, game):
        pass

class RComputerP(Player):
    def __init__(self, letter):
        super.__init__(letter)

    def get_move(self, game):
        square = random.choice(game.avilable_moves())
        return square

class HummanP(Player):
    def __init__(self, letter):
        super.__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:


