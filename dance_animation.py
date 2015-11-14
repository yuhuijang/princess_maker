# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((802,237), 0, 32)
pygame.display.set_caption('dance floor')



#background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('back.png', [0,0])

DISPLAYSURF.fill([255, 255, 255])
DISPLAYSURF.blit(BackGround.image, BackGround.rect)
Dan = pygame.image.load('dan2.png')
Hi = pygame.image.load('dan_end.png')
printImage = pygame.image.load('dan1.png')

catx = 100
caty = 120

direction = 'start'

while True: # the main game loop
    DISPLAYSURF.fill([255, 255, 255])
    DISPLAYSURF.blit(BackGround.image, BackGround.rect)


    if catx < 400:
        catx += 5
        DISPLAYSURF.blit(printImage,(catx,caty))

    if catx >= 400 and catx <500 :
        catx += 5
        DISPLAYSURF.blit(Dan,(400,caty))
    elif catx>=500:
        DISPLAYSURF.blit(Hi,(400,caty))



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
