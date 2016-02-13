from graphics import *
import math

makeGraphicsWindow(800, 600)

RADIUS = 15
HORT_GAP = 40
VERT_GAP = HORT_GAP*(math.sqrt(3)/2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def initBoard():
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
 
############################################################
# this function is called once to initialize your new world

def startWorld(world):
    world.board = initBoard()

 
############################################################
# this function is called every frame to update your world
 
def updateWorld(world):
	pass
 
############################################################
# this function is called every frame to draw your world
 
def drawWorld(world):
	shift = VERT_GAP / math.sqrt(3)
	t_shift = 12 * VERT_GAP / math.sqrt(3)

	for r in range(17):
		for c in range(17):
			if world.board[r][c] == -1:
				drawCircle(t_shift+(c*HORT_GAP), (r*VERT_GAP)+RADIUS+10, RADIUS, "black")
			elif world.board[r][c] != None:
				fillCircle(t_shift+(c*HORT_GAP), (r*VERT_GAP)+RADIUS+10, RADIUS, colors[world.board[r][c]])

		t_shift -= shift
 
############################################################

runGraphics(startWorld, updateWorld, drawWorld)