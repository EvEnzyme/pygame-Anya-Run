import pygame
from pygame.sprite import Sprite
from setting import BARRIER_POS, BARRIER_SPEED

class Barrier(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/obstacle/barrier.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=BARRIER_POS)
    
    def update(self):
        self.rect.x -= BARRIER_SPEED
        if self.rect.x <= -900:
            self.kill()