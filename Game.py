########################################
# CS63: Artificial Intelligence, Lab 3
# Spring 2016, Swarthmore College
########################################

from Queues import FIFO_Queue
from copy import deepcopy
from Players import *

class CChecker(object):
    def __init__(self):
        """The board is represented as a list of lists with length
        size. Blank locations are represented by the character '-'.
        The players locations are represented as 'B' and 'W'."""
        self.turn = None # should be in range(6)
        self.players = []
        self.board = []
        self.reset()

    def initBoard(self):
        board = []
        doc = open("init_board.txt", "r")

        for line in doc:
            line = line.strip()
            row = []
            for c in line:
                if c == '*':
                    row.append(None)
                else:
                    row.append(int(c)-1)
            board.append(row)
        return board

    def reset(self):
        """Resets the board to the starting configuration."""
        self.board = self.initBoard()


    def play(self, players):
        self.reset()
        self.players = players
        for i in range(6):
            self.players[i].setSide(i)

        
    def iterate(self):
        for player in self.players:
            row, col, drow, dcol = player.getMove(self.board)
            self.board[row][col] = -1
            self.board[drow][dcol] = player.side

    def getPossibleMoves(self, board):
        """Returns a list of all possible moves on the given board."""
        possible = []
        for row in range(self.size):
            for col in range(self.size):
                if board[row][col] == -1:
                    possible.append((row, col))
        return possible

    def getNextBoard(self, board, move, player):
        """Returns a new board showing how the given board would look after
        the move by player."""
        row, col = move
        if board[row][col] != '-':
            print("Error invalid move: %s" % (move))
            exit()
        nextBoard = deepcopy(board)
        nextBoard[row][col] = player
        return nextBoard

    def getNeighbors(self, row, col):
        """Returns a list of neighboring cells to the given row and col."""
        neighbors = []

        if row > 0:
            neighbors.append((row-1, col))
        if row < 16:
            neighbors.append((row+1, col))
        if col > 0:
            neighbors.append((row, col-1))
        if col < 16:
            neighbors.append((row, col+1))
        if row < 16 and col < 16:
            neighbors.append((row+1, col+1))
        if row > 0 and col > 0:
            neighbors.append((row-1, col-1))

        return neighbors

    def checkPiece(self,row,col,side):
        return self.board[row][col]==side

    def getDests(self,piece):
        """
        returns list of tupules of possible destinations
        """
        possible = []
        
        jumper= []
        row = piece[0]
        col = piece[1]

        queue = FIFO_Queue()

        queue.add(piece)
        neighbors = self.getNeighbors(piece[0],piece[1])

        """
            adds valid neighbors into list ofpossible
            adds blocked neighbors to check 
        """
        for neighbor in neighbors:
            curr = self.board[neighbor[0]][neighbor[1]]
            if curr != -1 or curr != None:
                possible.append(neighbor)

        while len(queue) != 0:
            curr = queue.get()
            jumper = []
            currNeighs = self.getNeighbors(curr[0],curr[1])

            for currNeigh in currNeighs:
                if self.board[currNeigh[0]][currNeigh[1]] ==-1:
                    jumper.append(curr)

            for jump in jumper:
                dest = self.findJump(curr[0],curr[1],jump[0],jump[1])
                if dest[0] == -1:
                    continue
                possible.append(dest)
                queue.add(dest)
        print "possible: ",possible
        print "current: ",piece
        return possible

    def checkMove(self, piece,drow,dcol):#rename getmove
    #make actal checkmove
        """
        returns true if move valid. false if not
        """
        poss = self.getDests(piece)

        if (drow,dcol) in poss:
            return True
        else:
            return False
        
        
    def findJump(self,row,col,brow,bcol):
        """
        for current row and col, and blocked neighbor brow, bcol:
        returns coordinate of jump destination
        returns -1,-1 if blocked there or unavailable
        """
        deltaRow = brow - row
        deltaCol = bcol - col
        destRow = deltaRow + brow
        destCol = deltaCol + bcol

        if destRow > 16 or destRow < 0 \
            or destCol > 16 or destCol < 0:
            return (-1,-1)

        if self.board[destRow][destCol] == -1:
            return (destRow,destCol)

        else:
            return (-1,-1)
