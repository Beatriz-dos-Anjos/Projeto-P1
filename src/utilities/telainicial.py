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

tela_inicial = pygame.image.load('assets/images/background/cenario2.jpeg').convert()
tela_inicial = pygame.transform.scale(tela_inicial, (largura,altura))


class Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/images/background/logo.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (219*3 ,116*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = 250, 50

todas_sprites = pygame.sprite.Group() 
logo = Logo()
todas_sprites.add(logo)

while True:
    relogio.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    

    tela.blit(tela_inicial, (0,0))


    todas_sprites.draw(tela)
    todas_sprites.update()

    pygame.display.flip()







