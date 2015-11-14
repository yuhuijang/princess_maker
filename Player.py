import random, sys, time, math, pygame
from pygame.locals import *

FPS = 30
WIN_WIDTH = 640
WIN_HEIGHT = 480
HALF_WIN_WIDTH = int(WIN_WIDTH/2)
HALF_WIN_HEIGHT = int(WIN_HEIGHT/2)

GLASSCOLOR = (24, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

CAMERASLACK = 90
MOVERATE = 9

START_SIZE = 25
GAME_OVER_TIME = 4
MAX_HEALTH = 3

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_PLY_IMG, R_PLY_IMG, GRASS_IMG

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('gameicon.png'))
    DISPLAYSURF = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    pygame.display.set_caption('squirrel Eat Squirrel')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    L_PLY_IMG = pygame.image.load('squirrel.png')
    R_PLY_IMG = pygame.transform.flip(L_PLY_IMG, True, False)
    GRASS_IMG = []
    for i in range(1, 5):
        GRASS_IMG.append(pygame.image.load('grass%s.png'% i))
    while True:
        runGame()

def runGame():
    gameOverMode = False
    winMode = False

    #게임에 필요한 글씨를 쓰기위한 surface를 만든다.
    gameOverSurf = BASICFONT.render('Game Over', True, WHITE)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.center = (HALF_WIN_WIDTH, HALF_WIN_HEIGHT)

    winSurf = BASICFONT.render('You have achived OMEGA SQUIRREL!', True, WHITE)
    winRect = winSurf.get_rect()
    winRect.center = (HALF_WIN_WIDTH, HALF_WIN_HEIGHT)

    winSurf2 = BASICFONT.render('(Press "r" to restart.)', True, WHITE)
    winRect2 = winSurf2.get_rect()
    winRect2.center = (HALF_WIN_WIDTH, HALF_WIN_HEIGHT + 30)

    camerax = 0
    cameay = 0

    grassObjs = []

    platerObj = {'surface': pygame.transform.scale(),
                 'facing': LEFT,
                 'size': START_SIZE,
                 'x': HALF_WIN_WIDTH,
                 'y': HALF_WIN_HEIGHT,
                 'bounce': 0,
                 'health': MAX_HEALTH}
