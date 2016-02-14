from graphics import *
from Players import *
from Game import CChecker
import math

makeGraphicsWindow(800, 600)

RADIUS = 15
HORT_GAP = 40
VERT_GAP = HORT_GAP*(math.sqrt(3)/2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
 
############################################################
# this function is called once to initialize your new world

def startWorld(world):
	world.start = True
	world.game = CChecker()
	players = []
	for i in range(6):
		players.append(HumanPlayer(world.game))
	world.game.play(players)

 
############################################################
# this function is called every frame to update your world
 
def updateWorld(world):
	if not world.start:
		world.game.iterate()
	else:
		world.start = False
 
############################################################
# this function is called every frame to draw your world
 
def drawWorld(world):
	shift = VERT_GAP / math.sqrt(3)
	t_shift = 12 * VERT_GAP / math.sqrt(3)

	for r in range(17):
		for c in range(17):
			if world.game.board[r][c] == -1:
				drawCircle(t_shift+(c*HORT_GAP), (r*VERT_GAP)+RADIUS+10, RADIUS, "black")
			elif world.game.board[r][c] != None:
				fillCircle(t_shift+(c*HORT_GAP), (r*VERT_GAP)+RADIUS+10, RADIUS, colors[world.game.board[r][c]])

		t_shift -= shift
 
############################################################

runGraphics(startWorld, updateWorld, drawWorld)