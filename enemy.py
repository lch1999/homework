
# coding: utf-8

# In[ ]:


import pygame, sys
#from pygame.locals import *
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        
        
        pygame.sprite.Sprite.__init__(self)       
        
        
        self.image = pygame.image.load("xiaodiji.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), randint( -5 * self.height, 0)
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
    def reset(self):
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), randint( -5 * self.height, 0)
        

