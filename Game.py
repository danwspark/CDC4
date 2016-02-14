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

        
    def iterate(self, playerNum):
        player = self.players[playerNum]
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
        if row > 16 or col > 16:
            return False
        return self.board[row][col]==side

    def getDests(self,piece):
        """
        returns list of tuples of possible destinations
        """
        possible = []
        
        jumper= []
        row = piece[0]
        col = piece[1]

        queue = FIFO_Queue()
        visited = set()

        queue.add(piece)
        neighbors = self.getNeighbors(piece[0],piece[1])

        """
            adds valid neighbors into list ofpossible
            adds blocked neighbors to check 
        """
        for (r, c) in neighbors:
            neighbor = self.board[r][c]
            if neighbor == -1:
                possible.append((r, c))

        while len(queue) != 0:
            curr = queue.get()
            visited.add(curr)
            jumper = []
            currNeighs = self.getNeighbors(curr[0],curr[1])

            for (r,c) in currNeighs:
                if self.board[r][c] == 0:
                    jumper.append((r,c))
            for jump in jumper:
                dest = self.findJump(curr,jump)
                if dest[0] == -1 or dest in visited:
                    continue
                possible.append(dest)
                queue.add(dest)
        print "possible: ",possible
        print "current: ",piece
        return possible

    def checkMove(self, piece,dest,side):#rename getmove
    #make actal checkmove
        """
        returns true if move valid. false if not
        """
        drow = dest[0]
        dcol = dest[1]
        poss = self.getDests(piece)
        if len(poss) == 0:
            return -1
        elif (drow,dcol) in poss:
            return 1
        elif (drow,dcol) not in poss:
            return 0
        
    def findJump(self,curr,block):
        """
        for current row and col, and blocked neighbor brow, bcol:
        returns coordinate of jump destination
        returns -1,-1 if blocked there or unavailable
        """
        row = curr[0]
        col = curr[1]
        brow = block[0]
        bcol = block[1]
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

def main():
    game = CChecker()
    players = []
    for i in range(6):
        players.append(HumanPlayer(game))
    game.play(players)

    game.iterate()

           
if __name__ == '__main__':
    main()