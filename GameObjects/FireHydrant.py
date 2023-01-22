import pygame
from random import randint
from pygame.sprite import Sprite
from setting import FIRE_HYDRANT_SPEED, FIRE_HYDRANT_SIZE, FIRE_HYDRANT_POS, FIRE_HYDRANT_RANDOM_OFFSET

class FireHydrant(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/obstacle/fire_hydrant.png').convert_alpha()
        x, y = FIRE_HYDRANT_POS
        x = randint(x-FIRE_HYDRANT_RANDOM_OFFSET, x+FIRE_HYDRANT_RANDOM_OFFSET)
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def update(self):
        self.rect.x -= FIRE_HYDRANT_SPEED
        if self.rect.x <= -900:
            self.kill() # this is a pygame sprite thing