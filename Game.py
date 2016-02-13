########################################
# CS63: Artificial Intelligence, Lab 3
# Spring 2016, Swarthmore College
########################################

from Queues import FIFO_Queue
from copy import deepcopy
from Players import *

def main():
    game = CChecker(17)
    print game
    
    p1 = HumanPlayer(game)
    p2 = HumanPlayer(game)
    p3 = HumanPlayer(game)
    p4 = HumanPlayer(game)
    p5 = HumanPlayer(game)
    p6 = HumanPlayer(game)

    game.playOneGame(p1, p2, p3, p4, p5, p6)
    

class CChecker(object):
    def __init__(self):
        """The board is represented as a list of lists with length
        size. Blank locations are represented by the character '-'.
        The players locations are represented as 'B' and 'W'."""
        self.turn = None # should be in range(6)
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
<<<<<<< HEAD
        self.board = []
        for i in range(self.size):
            self.board.append(['-']*self.size)
    """
||||||| merged common ancestors
        self.board = []
        for i in range(self.size):
            self.board.append(['-']*self.size)
"""
=======
        self.board = initBoard()
"""
>>>>>>> 3792f3f18a236326c24006b9a7d25c8e3b06db2b
    def __str__(self):
        #Returns a string representing the board.
        result = "\n"
        side = "black   "
        result += " "*self.size +  "white\n"
        for i in range(self.size):
            result +=  " " * i + side[i] + "  "
            for j in range(self.size-1):
                result += self.board[i][j] + " "
            result += self.board[i][self.size-1] + "  " + side[i] + "\n"
        result += " "*(int(2*self.size)) + "white"
        return result
        """


    def playOneGame(self, player1, player2, p3, p4, p5, p6, show=True):

    def play(self, players):
        pass

    def iterate(self):
        pass

    def playOneGame(self, player1, player2, show=True):

        """Plays a game and returns winner."""
        self.reset()
        player1.setSide(0)
        player2.setSide(1)
        p3.setSide(2)
        p4.setSide(3)
        p5.setSide(4)
        p6.setSide(5)
        print("%s vs %s" % (player1.name, player2.name))
        while True:
            if show:
                print(self)
                print("Player 0's turn")
            self.turn = 0
            row, col = player1.getMove(self.board)
            self.board[row][col] = self.turn
            #print "score for black: ",player1.eval(self.board)
            #connected = self.countConnected(self.board, self.turn)
            #print "%s connected: %d" % (self.turn, connected)
            if show:
                print("Made move (%d, %d)" % (row, col))
            if self.blackWins(self.board): 
                winner = 0
                break
            if show:
                print(self)
                print("Player 1's turn")
            self.turn = 1
            row, col = player2.getMove(self.board)
            
            self.board[row][col] = self.turn
            #connected = self.countConnected(self.board, self.turn)
            #print "%s connected: %d" % (self.turn, connected)
            if self.whiteWins(self.board): 
                winner = 'W'
                break
        if show:
            print(self)
            print("%s wins" % self.turn)
        return winner


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

    def blackWins(self, board):
        """Returns True if black player wins, otherwise False."""
        queue = FIFO_Queue()
        visited = set()
        # Add all locations of black pieces in the leftmost col to queue
        for row in range(self.size):
            if board[row][0] == 'B':
                queue.add((row, 0))
        # Try to find a path to the rightmost col
        while len(queue) > 0:
            row, col = queue.get()
            visited.add((row, col))
            for n in self.getNeighbors(row, col):
                r, c = n
                if board[r][c] != 'B': continue
                if c == self.size-1: return True
                if n in visited or n in queue:
                    continue
                queue.add(n)
        return False

    def whiteWins(self, board):
        """Returns True if white player wins, otherwise False."""
        queue = FIFO_Queue()
        visited = set()
        # Add all locations of white pieces n the top row to queue
        for col in range(self.size):
            if board[0][col] == 'W':
                queue.add((0, col))
        # Try to find a path to the bottom row
        while len(queue) > 0:
            row, col = queue.get()
            visited.add((row, col))
            for n in self.getNeighbors(row, col):
                r, c = n
                if board[r][c] != 'W': continue
                if r == self.size-1: return True
                if n in visited or n in queue:
                    continue
                queue.add(n)
        return False


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
        neighbors = getNeighbors(piece[0],piece[1])

        """
            adds valid neighbors into list ofpossible
            adds blocked neighbors to check 
        """
        for neighbor in neighbors:
            curr = self.board[neighbor[0]][neighbor[1]]
            if curr != -1 or curr != None:
                possible.append(curr)

        while len(queue) != 0:
            curr = queue.get()
            jumper = []
            currNeighs = getNeighbors(curr[0],curr[1])

            for currNeigh in currNeighs:
                if self.board[currNeigh[0]][currNeigh[1]] ==-1:
                    jumper.append(curr)

            for jump in jumper:
                dest = findJump(curr[0],curr[1],jump[0],jump[1])
                if dest[0] == -1:
                    continue
                possible.append(dest)
                queue.add(dest)

    def checkMove(self, piece,drow,dcol):#rename getmove
    #make actal checkmove
        """
        returns true if move valid. false if not
        """
        poss = getDests(piece)

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


    def countConnected(self, board, side):
        """Counts how many pieces for the given side touch another piece
        of the same side."""
        q = FIFO_Queue()
        visited = set()
        connected = 0

        #get all pieces of one color on the board
        for row in range(self.size):
            for col in range(self.size):
                if board[row][col] == side:
                    q.add( (row,col) )

        while len(q) > 0:
            row, col = q.get()
            if (row,col) not in visited:
                visited.add( (row,col) )
                isConnected = False
                for neighbor in self.getNeighbors(row,col):
                    if board[ neighbor[0] ][ neighbor[1] ] == side:
                        isConnected = True
                if isConnected:
                    connected += 1

        return connected

if __name__ == '__main__':
    main()
