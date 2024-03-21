import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 1000
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Seleção de Personagem')

relogio = pygame.time.Clock()
FPS = 45

tela_selecao = pygame.image.load('assets/images/background/selecao/image.png').convert()
tela_selecao = pygame.transform.scale(tela_selecao, (largura,altura))


fonte = pygame.font.Font(None, 36)
branco = (255, 255, 255)

personagem_1 = fonte.render("Pressione 1 para selecionar", True, branco)
personagem_2 = fonte.render("Pressione 2 para selecionar", True, branco)

