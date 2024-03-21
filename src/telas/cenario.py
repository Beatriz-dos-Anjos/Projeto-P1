import pygame
from pygame.locals import *


class Fundo_do_jogo():
    def __init__(self, tela, altura, largura):
        self.frame_atual = 0
        self.frame_1 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_1.jpg')
        self.frame_2 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_2.jpg')
        self.frame_3 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_3.jpg')
        self.frame_4 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_4.jpg')
        self.frame_5 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_5.jpg')
        self.frame_6 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_6.jpg')
        self.frame_7 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_7.jpg')
        self.frame_8 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_8.jpg')
        self.frame_9 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_9.jpg')
        self.frame_10 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_10.jpg')
        self.frame_11 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_11.jpg')
        self.frame_12 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_12.jpg')
        self.frame_13 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_12.jpg')
        self.frame_14 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_11.jpg')
        self.frame_15 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_10.jpg')
        self.frame_16 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_9.jpg')
        self.frame_17 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_8.jpg')
        self.frame_18 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_7.jpg')
        self.frame_19 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_6.jpg')
        self.frame_20 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_5.jpg')
        self.frame_21 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_4.jpg')
        self.frame_22 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_3.jpg')
        self.frame_23 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_2.jpg')
        self.frame_24 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_1.jpg')
        self.frames = [self.frame_1, self.frame_2, self.frame_3, self.frame_4, self.frame_5, self.frame_6, self.frame_7, self.frame_8,
                       self.frame_9, self.frame_10, self.frame_11, self.frame_12, self.frame_13, self.frame_14, self.frame_15, self.frame_16,
                       self.frame_17, self.frame_18, self.frame_19, self.frame_20, self.frame_21, self.frame_22, self.frame_23, self.frame_24]
        self.time = 125
        self.last_frame_time = 0
        self.largura = largura
        self.altura = altura
        self.tela = tela

    def atualizar_frame(self):
        if pygame.time.get_ticks() - self.last_frame_time >= self.time:
            self.last_frame_time = pygame.time.get_ticks()
            if self.frame_atual < len(self.frames) - 1:
                self.frame_atual += 1
            else:
                self.frame_atual = 0

    def battlegorund_print(self):
        self.atualizar_frame()

        escala = pygame.transform.scale(
            self.frames[self.frame_atual], (self.largura, self.altura))
        self.tela.blit(escala, (0, 0))
        