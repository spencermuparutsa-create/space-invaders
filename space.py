import pygame
pygame.init()

WIDTH = 1400
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))

space = pygame.image.load("lesson 4 - space invaders/images/space.png")
ship1 = pygame.image.load("lesson 4 - space invaders/images/spaceship_red.png")
ship1s = pygame.transform.scale(ship1,(90,80))
ship1r = pygame.transform.rotate(ship1s,90)
ship2 = pygame.image.load("lesson 4 - space invaders/images/spaceship_yellow.png")
ship2s = pygame.transform.scale(ship2,(90,80))
ship2r = pygame.transform.rotate(ship2s,270)

border = pygame.Rect(685,0,30,700)

red = pygame.Rect(70,140,90,80)
yellow = pygame.Rect(1200,140,90,80)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"black",border)
    #pygame.draw.rect(screen,"blue",red)
    screen.blit(ship1r,red)
    screen.blit(ship2r,yellow)
    pygame.display.update()