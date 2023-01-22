import pygame
from random import randint
from pygame.sprite import Sprite
from setting import PLANE_SPEED, PLANE_SIZE, PLANE_POS

class Plane(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/obstacle/plane.png').convert_alpha()
        x, y = PLANE_POS
        y = PLANE_POS[1] + randint(0,260)
        self.rect = self.image.get_rect(topleft = (x,y))
    
    def update(self):
        self.rect.x -= PLANE_SPEED
        if self.rect.x <= -900:
            self.kill()