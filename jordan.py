import pygame

class JORDAN:
    def __init__(self, tela, x, y): #propria instância da classe
        self.tela = tela
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/images/objetos_interagiveis/jordan.png')
        self.default_scale = (75, 80)
        self.image = pygame.transform.scale(self.image, self.default_scale)
