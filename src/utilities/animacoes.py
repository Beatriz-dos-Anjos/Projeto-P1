import pygame
from pygame.locals import *


def formar_lista_animacao(spritesheet, quantidade_frames, tamanho_x, tamanho_y, player):

    lista_de_frames = []

    for i in range(quantidade_frames):

        corte_da_imagem = i * tamanho_x
        imagem = spritesheet.subsurface(pygame.Rect(corte_da_imagem, 0, tamanho_x, tamanho_y))
        imagem_modificada = pygame.transform.scale(imagem, (tamanho_x * 2, tamanho_y * 2))
        imagem_espelhada = pygame.transform.flip(imagem_modificada, True, False)
        if player == 2:
            lista_de_frames.append(imagem_espelhada)
        else:
            lista_de_frames.append(imagem_modificada)
    
    return lista_de_frames
