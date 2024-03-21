import pygame
from pygame.locals import *


def formar_lista_animacao(spritesheet, quantidade_frames, tamanho_x, tamanho_y, posicao_x_do_corte, posicao_y_do_corte, player):

    lista_de_frames = []

    for i in range(quantidade_frames):

        corte_da_imagem = i * tamanho_x + posicao_x_do_corte
        imagem = spritesheet.subsurface(pygame.Rect(corte_da_imagem, posicao_y_do_corte, tamanho_x, tamanho_y))
        imagem_modificada = pygame.transform.scale(imagem, (tamanho_x * 2.5, tamanho_y * 2.5)) if player == 2 else pygame.transform.scale(imagem, (tamanho_x * 1.8, tamanho_y * 1.8))
        imagem_espelhada = pygame.transform.flip(imagem_modificada, True, False)
        if player == 2:
            lista_de_frames.append(imagem_espelhada)
        else:
            lista_de_frames.append(imagem_modificada)
    
    return lista_de_frames
