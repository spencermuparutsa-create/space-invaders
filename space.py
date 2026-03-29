import pygame
pygame.init()

WIDTH = 1400
HEIGHT = 700

FPS = 60    

screen = pygame.display.set_mode((WIDTH,HEIGHT))

space = pygame.image.load("lesson 4 - space invaders/images/space.png")
ship1 = pygame.image.load("lesson 4 - space invaders/images/spaceship_red.png")
ship1s = pygame.transform.scale(ship1,(90,80))
ship1r = pygame.transform.rotate(ship1s,90)
ship2 = pygame.image.load("lesson 4 - space invaders/images/spaceship_yellow.png")
ship2s = pygame.transform.scale(ship2,(90,80))
ship2r = pygame.transform.rotate(ship2s,270)
shoot = pygame.mixer.Sound("lesson 4 - space invaders/images/Gun+Silencer.mp3")
collide = pygame.mixer.Sound("lesson 4 - space invaders/images/Grenade+1.mp3")

RHealth = 10
YHealth = 10

border = pygame.Rect(685,0,30,700)

red = pygame.Rect(70,140,90,80)
yellow = pygame.Rect(1200,140,90,80)

font = pygame.font.SysFont("bradleyhand",30)

def redMove():
    if keys_pressed[pygame.K_w] and red.y> 0:
        red.y -= 3.5
    if keys_pressed[pygame.K_a] and red.x> 0:
        red.x -= 3.5
    if keys_pressed[pygame.K_s] and red.y< 620:
        red.y += 3.5
    if keys_pressed[pygame.K_d] and red.x< 610:
        red.x += 3.5
    
def yellowMove():

    if keys_pressed[pygame.K_UP] and yellow.y> 0:
        yellow.y -= 3.5
    if keys_pressed[pygame.K_LEFT] and yellow.x> 700:
        yellow.x -= 3.5
    if keys_pressed[pygame.K_DOWN] and yellow.y< 620:
        yellow.y += 3.5
    if keys_pressed[pygame.K_RIGHT] and yellow.x< 1310 :
        yellow.x += 3.5

    
clock = pygame.time.Clock()

redbullets = []
yellowbullets = []

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                bullet = pygame.Rect(red.x+90,red.y+40,10,7)
                shoot.play()
                redbullets.append(bullet)
            if event.key == pygame.K_RSHIFT:
                bullets = pygame.Rect(yellow.x,red.y+40,10,7)
                shoot.play()
                yellowbullets.append(bullets)
    screen.blit(space,(0,0))
    keys_pressed = pygame.key.get_pressed()
    redMove()
    yellowMove()
    pygame.draw.rect(screen,"black",border)
    #pygame.draw.rect(screen,"blue",red)
    screen.blit(ship1r,red)
    screen.blit(ship2r,yellow)
    textR = font.render("Health:" + str(RHealth),True,"white")
    textY = font.render("Health:" + str(YHealth),True,"white")
    screen.blit(textR,(10,10))
    screen.blit(textY,(1260,10))
    for rb in redbullets:
        pygame.draw.rect(screen,"red",bullet)
        rb.x+=9
        if yellow.colliderect(rb):
            collide.play()
            redbullets.remove(rb)
            YHealth -= 1
    for yb in yellowbullets:
        pygame.draw.rect(screen,"yellow",bullets)
        yb.x-=9

    pygame.display.update()