from graphics import *
makeGraphicsWindow(800, 600)
 
############################################################
# this function is called once to initialize your new world
 
def startWorld(world):
    world.ballX = 50
    world.ballY = 300
 
############################################################
# this function is called every frame to update your world
 
def updateWorld(world):
    world.ballX = world.ballX + 3
 
############################################################
# this function is called every frame to draw your world
 
def drawWorld(world):
    fillCircle(world.ballX, world.ballY, 50, "red")
 
############################################################
 
runGraphics(startWorld, updateWorld, drawWorld)