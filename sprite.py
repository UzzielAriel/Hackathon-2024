import pygame
HEIGHT = 500

imagestill = pygame.image.load("./Baby still.png")
imagewalking = pygame.image.load("./Baby walking.png")
imagestill = pygame.transform.scale(imagestill, (100, 100))
imagewalking = pygame.transform.scale(imagewalking, (100, 100))

class Sprite():
    def __init__(self):
        self.xv = 0
        self.yv = 0
        self.x = 10
        self.y = HEIGHT - 200
        self.width = 70
        self.height = 100
        self.walking = False
        # 0: stationary, 1: walking 
        self.icons = [imagestill,imagewalking]
        self.currentIcon = self.icons[0]

        self.obj = pygame.Rect(self.y, self.x, self.width, self.height)

    def tick(self,dis):
        # self.object = pygame.Rect()
        if self.walking == True:
            self.currentIcon = self.icons[1]
        else:
            self.currentIcon = self.icons[0]
        if pygame.key.get_pressed()[pygame.K_a]:
            self.left()
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.right()
        else:
            self.stopAnimation()
            self.xv = 0
        
        self.x += self.xv
        self.y += self.yv

        self.obj = pygame.Rect(self.x, self.y, self.width, self.height)

        self.gravity()

        self.draw(dis)

    def jump(self):
        self.yv = -20

    def gravity(self):
        self.yv += 1
        if abs((self.y) - 425) < 50:
            self.yv = 0
            self.y = 375

    def left(self):
        self.walking = True
        self.xv = -2

    def right(self):
        self.walking = True
        self.xv = 2

    def stopAnimation(self):
        self.walking = False

    def draw(self,dis):
        if self.walking == True:
            i = 1
        else:
            i = 0
        dis.blit(self.icons[i],(self.x,self.y))