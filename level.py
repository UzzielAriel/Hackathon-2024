import sprite
import pygame
import obstacle

class Level1:
   def __init__(self, dis, sprite):
       self.obstacles = []
       self.sprite = sprite
       self.dis = dis
       self.obstacles = [obstacle.Obstacles(width=300,height=50,x=200,y=330, typevh="v"), obstacle.Obstacles(width=50, height=122, x=200, y= 350, typevh="h"), obstacle.Obstacles(width=200, height=50, x=650, y=425, image=pygame.image.load("./trampoline.png")), obstacle.Obstacles(width=200, height=50, x=750, y=200, typevh="v", image=pygame.image.load("./bed.png"))]

   def draw(self):
       pygame.draw.line(self.dis, (0, 0, 0), [0, 475], [1000, 475], 5)
       for obs in self.obstacles:
           obs.draw(self.dis)
           if pygame.Rect.colliderect(self.sprite.obj, obs.obj):
            if obs.typevh == "v":
                if self.sprite.yv > 0:
                    self.sprite.yv =  0
                elif self.sprite.yv < 0:
                    self.sprite.yv = 0
                    self.sprite.y = self.sprite.y + obs.height
            elif obs.typevh == "h":
                if self.sprite.xv > 0:
                    self.sprite.xv = 0
                    self.sprite.x = obs.x - self.sprite.width
                if self.sprite.xv < 0:
                    self.sprite.xv = 0
                    self.sprite.x = obs.x + self.sprite.width
            elif obs.typevh == "t":
                if self.sprite.yv > 0:
                    self.sprite.yv = 0
                elif self.sprite.yv < 0:
                    self.sprite.yv = -self.sprite.yv
            elif obs.typevh == "b":
                if self.sprite.yv > 0:
                    self.sprite.yv = 0
                elif self.sprite.yv < 0:
                    self.sprite.yv = self.sprite.y + obs.height
                
                sprite.imagestill = pygame.image.load("./boy.png")
