import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#dimensões cenário
largura = 1000
altura = 600

#janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("arena")

#acrescentando o background
fundo = pygame.image.load('cenario2.jpeg')
tela.blit(fundo, (0,0))

#loop 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
