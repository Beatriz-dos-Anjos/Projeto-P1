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


def forrmar_chute_taylor(spritesheet, quantidade_frames, tamanho_x, tamanho_y, posicao_x_do_corte, posicao_y_do_corte, player):
    tamanhos = [42, 42, 60, 60, 69]
    
    lista_de_frames = []


    lista_de_frames.append(pygame.transform.flip(pygame.transform.scale(spritesheet.subsurface(pygame.Rect(posicao_x_do_corte, posicao_y_do_corte, 42, tamanho_y)), (tamanho_x * 2.5, tamanho_y * 2.5)), True, False))
    lista_de_frames.append(pygame.transform.flip(pygame.transform.scale(spritesheet.subsurface(pygame.Rect(posicao_x_do_corte + 42, posicao_y_do_corte, 42, tamanho_y)), (tamanho_x * 2.5, tamanho_y * 2.5)) , True, False))
    lista_de_frames.append(pygame.transform.flip(pygame.transform.scale(spritesheet.subsurface(pygame.Rect(posicao_x_do_corte + 84, posicao_y_do_corte, 60, tamanho_y)), (tamanho_x * 2.5, tamanho_y * 2.5)) , True, False))
    lista_de_frames.append(pygame.transform.flip(pygame.transform.scale(spritesheet.subsurface(pygame.Rect(posicao_x_do_corte + 144, posicao_y_do_corte, 60, tamanho_y)), (tamanho_x * 2.5, tamanho_y * 2.5)) , True, False))
    lista_de_frames.append(pygame.transform.flip(pygame.transform.scale(spritesheet.subsurface(pygame.Rect(posicao_x_do_corte + 204, posicao_y_do_corte, 69, tamanho_y)), (tamanho_x * 2.5, tamanho_y * 2.5)), True, False) )
    
    
    return lista_de_frames


