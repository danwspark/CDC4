########################################
# CS63: Artificial Intelligence, Lab 3
# Spring 2016, Swarthmore College
########################################

from Game import *
from random import choice, shuffle

class Player(object):
    """A base class for Hex players.  All players must implement the
    getMove method."""
    def __init__(self, side):
        self.human = None
        self.name = None
        self.side = side
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

class SimplePush(Player):
    """ Simple greedy Heuristic"""
    def __init__(self,game, side):
        Player.__init__(self, side)
        self.name = "SimplePush"
        self.game = game
        self.goal = self.setGoal(self.side)

    def setGoal(self, side):

        goal = None
        if side == 0:
            goal = (0,4)
        elif side == 1:
            goal = (4,0)
        elif side == 2:
            goal = (12,4)
        elif side == 3:
            goal = (16,12)
        elif side == 4:
            goal = (12,16)
        elif side == 5:
            goal = (4,12)
        return goal

    def getMove(self, board):
        """
        TODO: Implement some sort of randomizer.
        """
        pieces = self.game.findPieces(self.side)
        min = (None,None,float('inf'))
        for piece in pieces:
            currDist = self.game.pieceDist(piece,self.goal)
            dests = self.game.getDests(piece)
            for dest in dests:
                destDist = self.game.pieceDist(dest,self.goal)
                deltaDist = destDist - currDist
                if deltaDist < min[3]:
                    min = (piece,dest,deltaDist)
        start = min[0]
        end = min[1]
        return (start[0],start[1],end[0],end[1])

class RandomChoicePlayer(SimplePush):
    """Selects a random choice move."""
    def __init__(self, game, side):
        SimplePush.__init__(self, game, side)
        self.name = "RandomChoicePlayer"
        self.game = game
    def getMove(self, board):
        runs = 0
        while True:
            piece = choice(self.game.findPieces(self.side))
            dests = self.game.getDests(piece)
            if dests == []:
                continue
        
            dest = choice(dests)
            deltaDist = self.game.pieceDist(dest,self.goal) - self.game.pieceDist(piece,self.goal)

            if deltaDist <= 0:
                break
            # elif runs > 20:
            #     break
            runs += 1
        return (piece[0],piece[1],dest[0],dest[1])

class HumanPlayer(Player):
    """Selects a move chosen by the user."""
    def __init__(self, game, side):
        Player.__init__(self, side)
        #self.name = name
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
