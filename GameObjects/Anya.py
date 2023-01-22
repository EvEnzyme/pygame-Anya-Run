import pygame
from setting import ANYA_POS, ANYA_JUMP_SPEED

class Anya(pygame.sprite.Sprite):
    # for any pygame sprite, must have: self.image (texture), self.rect (hitbox), update()
    def __init__(self):
        super().__init__() #what does this do man
        self.frames = self.load_texture()
        self.animation_index = 0
        self.gravity = 0
        self.state = "ground" # can be air/ground

        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft = ANYA_POS)
        
    def load_texture(self):
        '''
            Return a list of pygame surfaces for the animation
            Should run only once on instantiation
        '''
        frame_1 = pygame.image.load('graphics/Anya/Anya1.png').convert_alpha()
        frame_2 = pygame.image.load('graphics/Anya/Anya2.png').convert_alpha()
        frame_3 = pygame.image.load('graphics/Anya/Anya3.png').convert_alpha()
        return [frame_1, frame_1, frame_2, frame_1, frame_3, frame_3]

    def play_input(self):
        '''
            Gets the input
            Should be called every frame
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.state == "ground":
            self.gravity = ANYA_JUMP_SPEED # Anya jump
            self.state = "air"

    def apply_gravity(self):
        '''
            Make Anya fall in the air
        '''
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.y >= ANYA_POS[1]:
            self.rect.y = ANYA_POS[1]
            self.state = "ground"

    def animate(self):
        if self.state == "air":
            self.image = self.frames[4]
        else:
            self.image = self.frames[int(self.animation_index)%6]
            self.animation_index += 0.3

    def update(self):
        '''
            Called every frame
        '''
        self.play_input()
        self.apply_gravity()
        self.animate()