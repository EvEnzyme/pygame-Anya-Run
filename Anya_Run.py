import pygame
from sys import exit

pygame.init() #initializing pygame 
screen = pygame.display.set_mode((800, 500))     # (width, height)
pygame.display.set_caption("Runner")    #changes the name of the window (was by default "pygame window")

#controlling the frame rate, ceiling and floor
clock = pygame.time.Clock()

#Creating text
#1. create a font
test_font = pygame.font.Font('graphics/Pixeltype.ttf', 50) #(font type, font size)
#2. create text surface
text_surface = test_font.render('Anya Run!', False, 'black') #(text, Anti-Aliasing, color)
text_rect = text_surface.get_rect(center = (400,120))

deadtxt_font = pygame.font.Font('graphics/Pixeltype.ttf', 80)
deadtxt_surface = deadtxt_font.render('Anya Got Hurt!!', False, 'black')
deadtxt_rect = deadtxt_surface.get_rect(center = (400, 140))
        

# Displaying images
    # Display surface -- the game window, what player actually see
    # (Regular) surf ace -- a single image, needs to be put on display surface to be visible, can have as many as wanted

# Plain color surface
# test_surface = pygame.Surface((100, 200))  # (w, h)
sky_surface = pygame.image.load('graphics/sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground1.png').convert_alpha()
anya1_surface = pygame.image.load('graphics/Anya1.png').convert_alpha()
anya2_surface = pygame.image.load('graphics/Anya2.png').convert_alpha()
anya3_surface = pygame.image.load('graphics/Anya3.png').convert_alpha()
fireHydrant_surface = pygame.image.load('graphics/fire_hydrant.png').convert_alpha()
end_surfae = pygame.image.load('graphics/end.png').convert_alpha()
#test_surface.fill('Blue')


anya_count = 0
anya_run = [anya1_surface, anya1_surface, anya2_surface, anya1_surface, anya3_surface, anya3_surface]

anya_rectangle = anya1_surface.get_rect(topleft = (100,283))
fireHydrant_rect = fireHydrant_surface.get_rect(topleft = (800, 330))
ground_rect = ground_surface.get_rect(topleft = (0,100))
anya_gravity = 0

game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()             # opposite of pygame.init(), uninitialize pygame
            exit()                    # end the while loop when called, more secure than the break statement
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and anya_rectangle.y == 283:
                        anya_gravity = -20
        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                
                game_active = True

   # the position of the top left point of the surface
   # blit = block image transfer, putting a shape onto another shape (rectangular display surface)  
    screen.blit(sky_surface, (0,0))   # (surface to place, position) 
    screen.blit(ground_surface,(0,100))    
    screen.blit(text_surface, text_rect)
    

    # key = pygame.key.get_pressed()
    # if key[pygame.K_SPACE]:

    def update_pos():
        ground_rect.x -=8
        if ground_rect.x == -800:
            ground_rect.x = 0
            
        fireHydrant_rect.x -=8
        if fireHydrant_rect.x <= -90:
            fireHydrant_rect.x = 800

    if game_active:
        #animation:
        #ground move
        screen.blit(ground_surface, ground_rect)
        
        #fire hydrant move in the same speed as the ground
        screen.blit(fireHydrant_surface, fireHydrant_rect)
        
        # anya_rectangle.left += 1
        #anya animation
        anya_gravity +=1
        anya_rectangle.y += anya_gravity
    
        #as above but for anya

        #Collisions
        if anya_rectangle.y < 283:
            screen.blit(anya_run[4],anya_rectangle)
        if anya_rectangle.y >= 283:
            anya_rectangle.y = 283
            screen.blit(anya_run[int(anya_count)%6],anya_rectangle)
        update_pos()

        if anya_rectangle.colliderect (fireHydrant_rect):
            game_active = False

    if not game_active:    
        fireHydrant_rect.x = 800
        screen.blit(fireHydrant_surface, fireHydrant_rect)
        screen.blit(end_surfae, (0,0))
        screen.blit(deadtxt_surface, deadtxt_rect)

    anya_count += 0.3
    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)      # the while true loop should not run faster than 60 times per second
