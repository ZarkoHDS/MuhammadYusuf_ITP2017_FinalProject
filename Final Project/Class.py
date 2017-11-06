import pygame, sys, time
from pygame.locals import *
from pygame.sprite import *
from pygame import *
pygame.init()
class Car1(Sprite):
    def __init__(self, image_file, x,y):
        Sprite.__init__(self)
        self.image = pygame.image.load("Car down.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.left = x
        self.rect.top = y
    def move(self, direction):
        if direction:
            if direction == K_UP:
                self.y -= 3
                self.image = pygame.image.load('Car up.png')
                self.rect.left = self.x
                self.rect.top = self.y
            elif direction == K_DOWN:
                self.y += 3
                self.image=pygame.image.load('Car down.png')
                self.rect.left = self.x
                self.rect.top = self.y
            if direction == K_LEFT:
                self.x -= 3
                self.image=pygame.image.load('Car left.png')
                self.rect.left = self.x
                self.rect.top = self.y
            elif direction == K_RIGHT:
                self.x += 3
                self.image=pygame.image.load('Car right.png')
                self.rect.left = self.x
                self.rect.top = self.y

class Car2(Sprite):
    def __init__(self, image_file, x,y):
        Sprite.__init__(self)
        self.image = pygame.image.load("Car up.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.left = x
        self.rect.top = y

    def move(self, direction):
        if direction:
            if direction == K_UP:
                self.y -= 3
                self.image = pygame.image.load('Car up.png')
                self.rect.left = self.x
                self.rect.top = self.y
            elif direction == K_DOWN:
                self.y += 3
                self.image=pygame.image.load('Car down.png')
                self.rect.left = self.x
                self.rect.top = self.y
            if direction == K_LEFT:
                self.x -= 3
                self.image=pygame.image.load('Car left.png')
                self.rect.left = self.x
                self.rect.top = self.y
            elif direction == K_RIGHT:
                self.x += 3
                self.image=pygame.image.load('Car right.png')
                self.rect.left = self.x
                self.rect.top = self.y

class textrect(Sprite):
    def __init__(self, fontstyle, text, fontsize, xpos, ypos, R, B, G):
        Sprite.__init__(self)
        self.font = pygame.font.SysFont(fontstyle,fontsize)
        self.image = self.font.render(text, False, (R,G,B))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class Streetblocks(Sprite):
    def __init__(self,image,x,y):
        Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.left = self.x
        self.rect.top = self.y

class Finish(Sprite):
    def __init__(self,image,x,y):
        Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.left = self.x
        self.rect.top = self.y
