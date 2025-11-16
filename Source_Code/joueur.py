import pygame

class Joueur:
    def __init__(self, x,y, size=60):
        self.x=x
        self.y=y
        self.size=size
        self.color=(255,255,255)

    def position_initial(self,screen):
        joueur_init=pygame.draw.rect(screen,(255,255,255),(self.x,self.y,self.size,self.size),1)

    def deplacement(self,dx,dy,step=60):
        self.x+= dx*step
        self.y+= dy*step
        