import pygame

class Obstacles:
    def __init__(self,width=0,height=0,x=0,y=0,typevh="h",image=pygame.image.load("./obstacle.png")
) -> None:
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        self.typevh = typevh
        image = pygame.transform.scale(image, (width, height))
        self.image = image

        self.obj = pygame.Rect(x, y, width, height)

    def tick(self,dis):
        self.draw(dis)
        self.obj = pygame.Rect(self.x, self.y, self.width, self.height)

    def checkhit(self,sprite):
        if sprite.x >= self.x - self.width and sprite.x - self.width <= self.x and sprite.y >= self.y - self.height and sprite.y - self.height <= self.y:
            return True
        else:
            return False

    def draw(self,dis):
        dis.blit(self.image,(self.x,self.y))