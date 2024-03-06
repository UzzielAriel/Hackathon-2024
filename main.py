import pygame
import sprite
import level
import obstacle

background = pygame.image.load("./background.png")
background = pygame.transform.scale(background, (1000, 500))

WIDTH = 1000
HEIGHT = 500
dis = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
pygame.init()
run = True
baby = sprite.Sprite()

level1 = level.Level1(dis, baby)
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                baby.jump()

    dis.fill((255, 255, 255))
    dis.blit(background,(0,0))

    
    baby.tick(dis)
    level1.draw()
    pygame.display.update()

    clock.tick(240)