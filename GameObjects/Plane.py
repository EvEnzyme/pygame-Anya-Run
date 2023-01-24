import pygame
from random import randint
from pygame.sprite import Sprite
from setting import PLANE_SPEED, PLANE_SIZE, PLANE_POS, PLANE_OSCILLATION_SPEED
from math import sin

class Plane(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/obstacle/plane.png').convert_alpha()
        x, y = PLANE_POS
        self.y = PLANE_POS[1] + randint(0,260)
        self.rect = self.image.get_rect(topleft = (x,y))

        self.animation_index = 0
    
    def update(self):
        self.rect.x -= PLANE_SPEED
        if self.rect.x <= -900:
            self.kill()

        self.rect.y = self.y+int(25*sin(self.animation_index))
        self.animation_index += PLANE_OSCILLATION_SPEED