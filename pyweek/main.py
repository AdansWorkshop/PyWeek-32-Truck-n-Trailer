import pygame, sys, random, os

from pygame.key import get_mods
from buttons import *

pygame.init()
size = width, height = 480, 360
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Truck n Trailer')

font = pygame.font.Font(None, 48)

start_button = BorderedImageButton(215, 155, 50, 50, pygame.image.load("sprites/StartButton.png"), 2, (30, 30, 30))
play_again_button = BorderedImageButton(215, 170, 50, 50, pygame.image.load("sprites/PlayAgainButton.png"), 2, (30, 30, 30))
game_running = False
game_over = False

score = 0

truckrect = pygame.Rect(268, 15, 150, 200)
truckcollrect = pygame.Rect(truckrect.x, truckrect.y, truckrect.width, 160)
truckimage = pygame.image.load("sprites/Truck.png")
truckspeed = 16
truckF = pygame.image.load("sprites/Truck.png")
truckR = pygame.image.load("sprites/TruckTL.png")
truckL = pygame.image.load("sprites/TruckTR.png")

trailerrect = pygame.Rect(random.randrange(46, 300), 360, 150, 200)
trailerimage = pygame.image.load("sprites/Trailer.png")

bgSY1 = -360
bgSY2 = 0
bgS = pygame.image.load("sprites/BG.png")

clock = pygame.time.Clock()
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    if not game_running and start_button.clicked():
        game_running = True
    
    if game_over and play_again_button.clicked():
        game_over = False
        game_running = True
        trailerrect.x = random.randrange(30, 300)
        trailerrect.y = 360
        score = 0
        truckrect.x = 268
    
    if not game_over:    
        if bgSY1 >= 360:
            bgSY1 = -360
        if bgSY2 >= 360:
            bgSY2 = -360
    
        bgSY1 += truckspeed/2
        bgSY2 += truckspeed/2


    if game_running and not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and truckrect.x > 30 or keys[pygame.K_LEFT] and truckrect.x > 30:
            truckrect.x -= 3
            truckimage = truckL
        elif keys[pygame.K_d] and truckrect.x < 300 or keys[pygame.K_RIGHT] and truckrect.x < 300:
            truckrect.x += 3
            truckimage = truckR
        else:
            truckimage = truckF
        
        trailerrect.y -= 2

        if trailerrect.x <= truckrect.x + 15 and trailerrect.x >= truckrect.x - 15 and trailerrect.y < truckrect.bottom - 10:
            trailerrect.y = 360
            trailerrect.x = random.randrange(30, 300)
            score += 1
        if trailerrect.bottom == 0 or truckcollrect.colliderect(trailerrect):
            game_running = False
            game_over = True

    score_surface = font.render(str(score), True, (0, 0, 0))
    game_over_surf = font.render("Game Over", True, (187, 187, 187))

    screen.fill((0, 0, 0))
    screen.blit(bgS, (0, bgSY1))
    screen.blit(bgS, (0, bgSY2))
    screen.blit(pygame.transform.scale(truckimage, truckrect.size), truckrect.topleft)
    if not game_running and not game_over:
        start_button.draw(screen)
    elif game_running and not game_over:
        screen.blit(pygame.transform.scale(trailerimage, trailerrect.size), trailerrect.topleft)
        screen.blit(score_surface, (4, 4))
    if game_over:
        screen.blit(game_over_surf, (240 - (game_over_surf.get_width()//2), 140 - (game_over_surf.get_height()//2)))
        play_again_button.draw(screen)
    
    pygame.display.flip()

