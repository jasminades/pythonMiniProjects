import math
import random

class Player:
    def __init__(self,letter):
        #letter is x or o
        self.letter = letter

    def get_move(self,game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s  turn. Input move (0-9)  ')

            # checking that this is a correct value by trying to cast
            # if to an integer, and if it's not, then it's invalid
            # if that spot is not available on the board, it's also invalid

            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')
        return val
