from graphics import *
from Players import *
from Game import CChecker
import math

makeGraphicsWindow(800, 600)

RADIUS = 15
HORT_GAP = 40
VERT_GAP = HORT_GAP*(math.sqrt(3)/2)

SLEEPER_T = 0

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def myMousePressedFunction(world, mouseX, mouseY, button):
     for (x, y) in world.coords2pos:
     	(row, col) = world.coords2pos[(x, y)]

     	dist = math.sqrt((mouseX - x)**2 + (mouseY - y)**2)
     	if dist < RADIUS:
     		# clicked circle
     		if world.source == None:
     			# selecting source
     			# check if legit source
     			if world.game.checkPiece(row,col,world.turn):
     				dests = world.game.getDests((row, col))
     				if len(dests) > 0:
     					world.source = ((row, col))
     					world.highlight.append((x, y))
     					for dest in dests:
     						world.highlight.append(world.pos2coords[dest])
     		elif world.dest == None:
     			# selecting dest
     			# check if legit dest
     			dests = world.game.getDests(world.source)
     			if (row, col) in dests:
     				world.dest = ((row, col))
 
############################################################
# this function is called once to initialize your new world

def startWorld(world):
	world.game = CChecker()
	world.players = []
	for i in range(6):
		p = RandomChoicePlayer(world.game, i)
		# p.setSide(i)
		world.players.append(p)

	world.players[0] = HumanPlayer(world.game, 0)

	world.game.play(world.players)
	world.turn = -1

	world.source = None
	world.dest = None
	world.highlight = []
	world.pos2coords = {}
	world.coords2pos = {}

	world.sleeper = SLEEPER_T

	shift = VERT_GAP / math.sqrt(3)
	t_shift = 12 * VERT_GAP / math.sqrt(3)

	for r in range(17):
		for c in range(17):
			if world.game.board[r][c] != None:
				world.coords2pos[(t_shift+(c*HORT_GAP), (r*VERT_GAP)+RADIUS+10)] = (r, c)
				world.pos2coords[(r, c)] = (t_shift+(c*HORT_GAP), (r*VERT_GAP)+RADIUS+10)

		t_shift -= shift

	onMousePress(myMousePressedFunction)

############################################################
# this function is called every frame to update your world
 
def updateWorld(world):
	if world.turn != -1:
		if world.players[world.turn].human != True:
			
			if world.sleeper > 0:
				#wait by counter acting turn switch
				world.turn -= 1
				world.sleeper -= 1
			else:
				world.game.iterate(world.turn)
				# reset for next turn
				world.sleeper = SLEEPER_T
		else:
			if world.source == None or world.dest == None:
				# waiting on human to make turn
				world.turn -= 1 # counter act turn switch
			else:
				# human finished turn
				row, col = world.source
				drow, dcol = world.dest

				world.game.board[row][col] = -1
				world.game.board[drow][dcol] = world.turn
				world.highlight = []
				world.source = None
				world.dest = None

	world.turn += 1
	world.turn = world.turn % 6
 
############################################################
# this function is called every frame to draw your world
 
def drawWorld(world):

	for r in range(17):
		for c in range(17):
			if world.game.board[r][c] == -1:
				(x, y) = world.pos2coords[(r, c)]
				drawCircle(x, y, RADIUS, "black")
			elif world.game.board[r][c] != None:
				(x, y) = world.pos2coords[(r, c)]
				fillCircle(x, y, RADIUS, colors[world.game.board[r][c]])

	for (x, y) in world.highlight:
		fillCircle(x, y, RADIUS+1, "lightblue")

	drawString("Player %d's turn" % (world.turn+1), 10, 10)
 
############################################################

runGraphics(startWorld, updateWorld, drawWorld)