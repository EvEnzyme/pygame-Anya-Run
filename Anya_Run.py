import pygame
from sys import exit
from random import randint
from setting import WINDOW_SIZE, SCORE_POSITION, SKY_SPEED, GROUND_SPEED, BUILDING1_SPEED, BUILDING2_SPEED
from GameObjects.Anya import Anya
from GameObjects.FireHydrant import FireHydrant 
from GameObjects.Plane import Plane
from GameObjects.Barrier import Barrier

def display_score():
    #pygame.time.get_ticks() gives the time since the game started
    curr_time = (pygame.time.get_ticks()) // 1000 - start_time
    score_surf = deadtxt_font.render(str(curr_time)+"m", False, (64,64,64))
    score_rect = score_surf.get_rect(center = SCORE_POSITION)
    screen.blit(score_surf, score_rect)
    return curr_time

def update_background(obj1, obj2, obj_speed):
    # ground_rect_1.x -= GROUND_SPEED
    # ground_rect_2.x -= GROUND_SPEED
    # sky_rect_1.x -= SKY_SPEED
    # sky_rect_2.x -= SKY_SPEED
    # building1_rect_1.x-=BUILDING1_SPEED
    # building1_rect_2.x-=BUILDING1_SPEED
    # building2_rect_1.x-=BUILDING2_SPEED
    # building2_rect_2.x-=BUILDING1_SPEED
    obj1.x-=obj_speed
    obj2.x-=obj_speed

    if obj1.x <= -820 and obj2.x<=20:
        obj1.x = 0
        obj2.x = 820
   
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Anya Run")
start_time = 0

# clock object from pygame to control FPS, called in the game loop
clock = pygame.time.Clock()

# creating text
# 1. create a font
deadtxt_font = pygame.font.Font('graphics/Pixeltype.ttf', 80)
# 2. create text surface
deadtxt_surf = deadtxt_font.render('Anya Got Hurt!!', False, 'black')
deadtxt_rect = deadtxt_surf.get_rect(center = (400, 140))



sky_surf = pygame.image.load('graphics/background/sky.png').convert_alpha()
sky_rect_1 = sky_surf.get_rect(topleft = (0,0))
sky_rect_2 = sky_surf.get_rect(topleft = (800,0))

ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()
ground_rect_1 = ground_surf.get_rect(topleft = (0,0))
ground_rect_2 = ground_surf.get_rect(topleft = (820,0))

building1_surf = pygame.image.load('graphics/background/building1.png').convert_alpha()
building1_rect_1 = building1_surf.get_rect(topleft = (0,0))
building1_rect_2 = building1_surf.get_rect(topleft = (820,0))


building2_surf = pygame.image.load('graphics/background/building2.png').convert_alpha()
building2_rect_1 = building1_surf.get_rect(topleft = (0,0))
building2_rect_2 = building1_surf.get_rect(topleft = (820,0))

end_surface = pygame.image.load('graphics/end.png').convert_alpha()

anya = pygame.sprite.GroupSingle()
anya.add(Anya())
obstacles = pygame.sprite.Group()


game_active = True
# timers
# create a custom user event that is triggered in vertai time intervals
obstacle_timer = pygame.USEREVENT+1 #plus 1 because some events are reserved by pygame, +1 to avoid triggering those events
pygame.time.set_timer(obstacle_timer, 800)

print(building1_rect_2.w)
print(building2_rect_2.w)

curr_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()             # opposite of pygame.init(), uninitialize pygame
            exit()                    # end the while loop when called, more secure than the break statement
        
        if game_active:
            if event.type == obstacle_timer and game_active:
                ran_index = randint(0,10)
                if 0 <= ran_index <= 3:
                    obstacles.add(FireHydrant())
                if 4 <= ran_index <= 5:
                    obstacles.add(Barrier())
                if 6 <= ran_index <= 10:
                    obstacles.add(Plane())
        
        elif not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  
                game_active = True
                start_time = pygame.time.get_ticks()//1000
                obstacles.empty()

    if game_active:
        screen.blit(sky_surf, sky_rect_1)
        screen.blit(sky_surf, sky_rect_2)
        screen.blit(building2_surf, building2_rect_1)
        screen.blit(building2_surf, building2_rect_2)
        screen.blit(building1_surf, building1_rect_1)
        screen.blit(building1_surf, building1_rect_2)
        screen.blit(ground_surf, ground_rect_1)
        screen.blit(ground_surf, ground_rect_2)
        anya.draw(screen)
        obstacles.draw(screen)
        curr_time = display_score()

        update_background(sky_rect_1, sky_rect_2, SKY_SPEED)
        update_background(building1_rect_1, building1_rect_2, BUILDING1_SPEED)
        update_background(building2_rect_1, building2_rect_2, BUILDING2_SPEED)
        update_background(ground_rect_1,ground_rect_2,GROUND_SPEED)
        anya.update()
        obstacles.update()

        game_active = not pygame.sprite.spritecollide(anya.sprite,obstacles,False)

    if not game_active:
        screen.blit(end_surface, (0,-10))
        screen.blit(deadtxt_surf, deadtxt_rect)
        deadscore_font = pygame.font.Font('graphics/Pixeltype.ttf', 60)
        deadscore_surf = deadscore_font.render('Anya Traveled ' + str(curr_time) + 'm', False, 'black')
        deadscore_rect = deadscore_surf.get_rect(center = (400, 360))
        screen.blit(deadscore_surf, deadscore_rect)

    pygame.display.update()
    clock.tick(60)  # render at 60 FPS
