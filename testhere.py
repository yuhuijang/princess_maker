import math, sys
import pygame
from pygame.locals import *

#initialization
pygame.init()

#Display Settings
DISPLAYSURF = pygame.display.set_mode((640,400),0,32)
pygame.display.set_caption('Background')

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#Background_img Settings
background = pygame.image.load('m_heya.png')
backgroundRect = background.get_rect()

#Charator Settings in room
musume = pygame.image.load('musume.png')
mesumeRect = musume.get_rect()

#Schedule Button Settings
schedule = pygame.image.load('schedule.png')

#Summer dress
summer_dress = pygame.image.load('musume_natu.png')


#Mouse index
LEFT = 1
RIGHT = 3

dress_type = None

#Main program
while True:
#Background
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(background, backgroundRect)
    DISPLAYSURF.blit(musume, mesumeRect)

    if dress_type == "summer_dress":
        DISPLAYSURF.blit(summer_dress,mesumeRect)
    else:
        DISPLAYSURF.blit(musume, mesumeRect)

#Exit
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
            print 'Hi,Summer'
            dress_type = 'summer_dress'
        elif event.type == MOUSEBUTTONUP and event.button == LEFT:
            DISPLAYSURF.blit(summer_dress,mesumeRect)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()