import pygame
from pygame.locals import *
from sys import exit



pygame.init()

largura = 1000
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Tela inicial')

relogio = pygame.time.Clock()
FPS = 45

tela_inicial = pygame.image.load('assets/images/background/fundoembaçado2.png').convert()
tela_inicial = pygame.transform.scale(tela_inicial, (largura,altura))


class Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF1.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF2.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF3.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF4.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF5.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF6.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF7.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF8.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF9.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF10.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF11.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF12.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF13.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF14.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF15.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF16.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF17.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF18.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF19.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF20.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF21.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF22.png'))
        self.sprites.append(pygame.image.load('assets/images/background/spritesinicial/SOF23.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (219*7 ,116*7))
        self.rect = self.image.get_rect()
        self.rect.topleft = -(320), -(200)
        
    def update(self):
        self.atual = self.atual + 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (219*7,116*7))

class Start(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/images/background/start/start1.png'))
        self.sprites.append(pygame.image.load('assets/images/background/start/start2.png'))
        self.sprites.append(pygame.image.load('assets/images/background/start/start3.png'))
        self.sprites.append(pygame.image.load('assets/images/background/start/start4.png'))
        self.sprites.append(pygame.image.load('assets/images/background/start/start5.png'))
        self.sprites.append(pygame.image.load('assets/images/background/start/start6.png'))
        self.sprites.append(pygame.image.load('assets/images/background/start/start7.png'))
        self.sprites.append(pygame.image.load('assets/images/background/start/start8.png'))
        self.sprites.append(pygame.image.load('assets/images/background/start/start9.png'))
        self.sprites.append(pygame.image.load('assets/images/background/start/start10.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (219*2 ,116*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = 280, 378
    
    def update(self):
        self.atual = self.atual + 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (219*2,116*2))

class End(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/images/background/end/1.png'))
        self.sprites.append(pygame.image.load('assets/images/background/end/2.png'))
        self.sprites.append(pygame.image.load('assets/images/background/end/3.png'))
        self.sprites.append(pygame.image.load('assets/images/background/end/4.png'))
        self.sprites.append(pygame.image.load('assets/images/background/end/5.png'))
        self.sprites.append(pygame.image.load('assets/images/background/end/6.png'))
        self.sprites.append(pygame.image.load('assets/images/background/end/7.png'))
        self.sprites.append(pygame.image.load('assets/images/background/end/8.png'))
        self.sprites.append(pygame.image.load('assets/images/background/end/9.png'))
        self.sprites.append(pygame.image.load('assets/images/background/end/10.png'))        

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (219*2 ,116*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = 280, 430

    def update(self):
        self.atual = self.atual + 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (219*2,116*2))
        
sprites = pygame.sprite.Group() 







