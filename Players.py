########################################
# CS63: Artificial Intelligence, Lab 3
# Spring 2016, Swarthmore College
########################################

from Game import *
from random import choice, shuffle

class Player(object):
    """A base class for Hex players.  All players must implement the
    getMove method."""
    def __init__(self):
        self.human = None
        self.name = None
        self.side = None
        self.game = None
        self.wins = 0
        self.losses = 0

    def setSide(self, side):
        self.side = side

    def otherSide(self, side):
        """
        retuns a list of 'other sides'
        """
        antiSide = range(6)
        antiSide.remove(side)
        return antiSide
    def won(self):
        self.wins += 1
    def lost(self):
        self.losses += 1
    def results(self):
        result = self.name
        result += " Wins:" + str(self.wins)
        result += " Losses:" + str(self.losses)
        return result
    def getMove(self, board):
        """
        Given the current board, should return a valid move.
        """
        raise NotImplementedError()

class RandomChoicePlayer(Player):
    """Selects a random choice move."""
    def __init__(self, game):
        Player.__init__(self)
        self.name = "RandomChoicePlayer"
        self.game = game
    def getMove(self, board):
        return choice(self.game.getPossibleMoves(board))

class RandomShufflePlayer(Player):
    """Shuffles the possible moves, then selects the first possible move."""
    def __init__(self, game):
        Player.__init__(self)
        self.name = "RandomShufflePlayer"
        self.game = game
    def getMove(self, board):
        possible = self.game.getPossibleMoves(board)
        shuffle(possible)
        return possible[0]

class HumanPlayer(Player):
    """Selects a move chosen by the user."""
    def __init__(self, game, name="HumanPlayer"):
        Player.__init__(self)
        self.name = name
        self.game = game
        self.human = True

    def getMove(self, board):
        print("\n%s's turn" % (self.name))
        while True:
            row, col = input("Enter row, col of the piece you want to move: ")
            if self.game.checkPiece(row,col,self.side) == False :#must be implemented
                print "That is not your piece. Try again"
                continue
            drow, dcol = input ("Where do you want to move it?")
            response = -1
            while True:
                response = self.game.checkMove((row,col),(drow,dcol),self.side)
                if response == 0:
                    print "Invalid Move. Try again!"
                    drow, dcol = input ("Where do you want to move it?")
                else:
                    break
            if response == -1:
                print "Invalid move. Choose another piece to move."
                continue

            return (row, col, drow, dcol)
