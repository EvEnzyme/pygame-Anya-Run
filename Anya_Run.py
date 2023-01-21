import pygame
from sys import exit
from random import randint
from setting import *

def display_score():
    #pygame.time.get_ticks() gives the time since the game started
    curr_time = (pygame.time.get_ticks())//1000 - start_time
    score_surf = test_font.render(f'{curr_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = SCORE_POSITION)
    screen.blit(score_surf, score_rect)

 #define a method that takes a list of objects that are appended at random timing (between 900-1200)
 #for ex. there will have multiple fire hydrants on the screen, all listed in this list
 #this function moves everything to the left at the same speed
def ob_movement(ob_list):
    '''Moves every obstacle in the ob_list'''
    if ob_list:
        for ob_rect in ob_list:
            if ob_rect.w == BARRIER_SIZE[0]:
                ob_rect.x -= BARRIER_SPEED
                screen.blit(barrier_surface, ob_rect)
            elif ob_rect.w == FIRE_HYDRANT_SIZE[0]:
                ob_rect.x -= FIRE_HYDRANT_SPEED
                screen.blit(fireHydrant_surface, ob_rect)
            elif ob_rect.w == PLANE_SIZE[0]:
                ob_rect.x -= PLANE_SPEED
                screen.blit(plane_surface, ob_rect)
        return  ob_list
    else:
        return []

pygame.init() #initializing pygame 
screen = pygame.display.set_mode(WINDOW_SIZE)     # (width, height)
pygame.display.set_caption("Runner")    #changes the name of the window (was by default "pygame window")
start_time = 0

#controlling the frame rate, ceiling and floor
clock = pygame.time.Clock()

#Creating text
#1. create a font
test_font = pygame.font.Font('graphics/Pixeltype.ttf', 50) #(font type, font size)
#2. create text surface
# text_surface = test_font.render('Anya Run!', False, 'black') #(text, Anti-Aliasing, color)
# text_rect = text_surface.get_rect(center = (400,120))

deadtxt_font = pygame.font.Font('graphics/Pixeltype.ttf', 80)
deadtxt_surface = deadtxt_font.render('Anya Got Hurt!!', False, 'black')
deadtxt_rect = deadtxt_surface.get_rect(center = (400, 140))
        

# Displaying images
    # Display surface -- the game window, what player actually see
    # (Regular) surf ace -- a single image, needs to be put on display surface to be visible, can have as many as wanted

# Plain color surface
# test_surface = pygame.Surface((100, 200))  # (w, h)
sky_surface = pygame.image.load('graphics/sky.png').convert_alpha()
sky_rect_1 = sky_surface.get_rect(topleft = (0,0))
sky_rect_2 = sky_surface.get_rect(topleft = (800,0))

ground_surface = pygame.image.load('graphics/ground1.png').convert_alpha()
ground_rect_1 = ground_surface.get_rect(topleft = (0,100))
ground_rect_2 = ground_surface.get_rect(topleft = (790,100))

anya1_surface = pygame.image.load('graphics/Anya1.png').convert_alpha()
anya2_surface = pygame.image.load('graphics/Anya2.png').convert_alpha()
anya3_surface = pygame.image.load('graphics/Anya3.png').convert_alpha()
anya_run = [anya1_surface, anya1_surface, anya2_surface, anya1_surface, anya3_surface, anya3_surface]
anya_count = 0

#obstacles
ob_rect_list = []
barrier_surface = pygame.image.load('graphics/barrier.png').convert_alpha()
fireHydrant_surface = pygame.image.load('graphics/fire_hydrant.png').convert_alpha()
end_surface = pygame.image.load('graphics/end.png').convert_alpha()
plane_surface = pygame.image.load('graphics/plane.png').convert_alpha()
#test_surface.fill('Blue')

rect1 = barrier_surface.get_rect()
rect2 = fireHydrant_surface.get_rect()
rect3 = plane_surface.get_rect()

ob_type = [fireHydrant_surface, barrier_surface, plane_surface]
ob_starting_y = [FIRE_HYDRANT_POS[1], BARRIER_POS[1], PLANE_POS[1]]


anya_rectangle = anya1_surface.get_rect(topleft = (100,283))
# barrier_rect = barrier_surface.get_rect(topleft = (1150, 305))
plane_rect = plane_surface.get_rect(topleft = (650, 100))
anya_gravity = 0

game_active = True

#timers
#create a custom user event that is triggered in vertai time intervals
obstacle_timer = pygame.USEREVENT+1 #plus 1 because some events are reserved by pygame, +1 to avoid triggering those events
pygame.time.set_timer(obstacle_timer, 900)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()             # opposite of pygame.init(), uninitialize pygame
            exit()                    # end the while loop when called, more secure than the break statement
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and anya_rectangle.y == 283:
                    anya_gravity = ANYA_JUMP_SPEED
            if event.type == obstacle_timer and game_active:
                ran_index = randint(0,2)
                if ran_index == 2:
                    ob_rect_list.append((ob_type[ran_index]).get_rect(topleft = (randint(900, 1100), ob_starting_y[ran_index]+randint(0,260))))
                else:
                    ob_rect_list.append((ob_type[ran_index]).get_rect(topleft = (randint(900, 1100), ob_starting_y[ran_index])))
        
        elif not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  
                game_active = True
                start_time = pygame.time.get_ticks()//1000
            

   # the position of the top left point of the surface
   # blit = block image transfer, putting a shape onto another shape (rectangular display surface)  
   # # (surface to place, position)   
    

    # key = pygame.key.get_pressed()
    # if key[pygame.K_SPACE]:

    def update_pos():
        ground_rect_1.x -= GROUND_SPEED
        ground_rect_2.x -= GROUND_SPEED
        sky_rect_1.x -= SKY_SPEED
        sky_rect_2.x -= SKY_SPEED

        if ground_rect_1.x <= -800 and ground_rect_2.x<=-10:
            ground_rect_1.x = 0
            ground_rect_2.x = 790
        if sky_rect_1.x <= -800 and sky_rect_2.x <= 0:
            sky_rect_1.x = 0
            sky_rect_2.x = 800
        # fireHydrant_rect.x -=10
        # if fireHydrant_rect.x <= -90:
        #     fireHydrant_rect.x = 800
        # barrier_rect.x -=10
        # if barrier_rect.x <= -200:
        #     barrier_rect.x = 800
        

    if game_active:
        #animation:
        #ground move
        screen.blit(sky_surface, sky_rect_1)
        screen.blit(sky_surface, sky_rect_2)
        screen.blit(ground_surface, ground_rect_1)
        screen.blit(ground_surface, ground_rect_2)
        #fire hydrant move in the same speed as the ground
        # screen.blit(barrier_surface, barrier_rect)
        # screen.blit(fireHydrant_surface, fireHydrant_rect)
        display_score()
        # screen.blit(text_surface, text_rect)
        
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

        #obstacle movement
        ob_rect_list = ob_movement(ob_rect_list)
        
        for ob_rect in ob_rect_list:
            if anya_rectangle.colliderect (ob_rect):
                game_active = False
                ob_rect_list.clear()

        
    if not game_active:
        screen.blit(end_surface, (0,0))
        screen.blit(deadtxt_surface, deadtxt_rect)

    anya_count += 0.3
    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)      # the while true loop should not run faster than 60 times per second
