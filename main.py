import pygame
from pygame.locals import *
from sys import exit
from taylor import Taylor_fighter
from kanye import Kanye_fighter
pygame.init()

# dimensões cenário
largura = 1000
altura = 600

# janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Swift of Fightwest")

# framerate do jogo
relogio = pygame.time.Clock()
FPS = 45

# acrescentando o background
fundo = pygame.image.load('assets/images/backgrounds/cenario2.jpeg')

# Função para desenhar o background
# Essa parte do código é essencial para ser chamada no loop, pois sem ela os personagens não se movimentam, a imagem deles é desenhada


def bg():
    escala = pygame.transform.scale(fundo, (largura, altura))
    tela.blit(escala, (0, 0))


# Criando os personagens
Taylor_Swift = Taylor_fighter(1, 200, 310)
Kanye_West = Kanye_fighter(2, 700, 310)

# loop
while True:
    relogio.tick(FPS)
    bg()
    # Interação de Combate
    Taylor_Swift.combate(tela)
    Kanye_West.combate(tela)
    # Movimento dos personagens
    Taylor_Swift.move(largura, altura)
    Kanye_West.move(largura, altura)
    # Desenhar os personagens
    Taylor_Swift.draw(tela)
    Kanye_West.draw(tela)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
