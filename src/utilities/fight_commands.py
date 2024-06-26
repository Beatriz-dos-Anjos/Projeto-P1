import pygame
from pygame.locals import *
from utilities.colisoes import colisao  # Não está pegando sem o utilities

pygame.init()
musica_de_soco = pygame.mixer.Sound(
    'assets/images/sounds/punch-140236.mp3')


def combate(rect, player, surface, posicao_oponente_x, posicao_oponente_y, barra_de_vida_oponente, barra_de_vida_player, inimigo_esta_defendendo):
    attacking_damage = 0
    attacked_or_not = False
    tipo_de_ataque = None
    defendendo_ou_nao = False

    keys = pygame.key.get_pressed()

    if player == 1:  # COMANDOS DE ATAQUE PARA O PLAYER 1

        # ATAQUE DE SOCO
        if keys[pygame.K_e]:

            attacking_damage = 9 if inimigo_esta_defendendo == False else 1  # Quantidade de dano
            attacked_or_not = True  # variável para se ele atacou ou não

            area_de_colisao = pygame.Rect(
                rect.x + 165, rect.y, 80, 100)  # área de colisão

            # desenha a hitbox do ataque
            #pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
            # desenha a hit box do personagem inimigo
            posicao = pygame.Rect(posicao_oponente_x,
                                  posicao_oponente_y, 80, 180)
            tipo_de_ataque = 1  # vai servir para a animação, 1 == Soco

            # invoca a função para verificar se houve colisão entre o golpe e o inimigo
            colisao(area_de_colisao, posicao,
                    attacking_damage, barra_de_vida_oponente)

            musica_de_soco.play()
        # ATAQUE DE CHUTE
        if keys[pygame.K_r]:

            attacking_damage = 13 if inimigo_esta_defendendo == False else 3
            attacked_or_not = True

            area_de_colisao = pygame.Rect(rect.x + 140, rect.y + 60, 80, 150)

            #pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
            posicao = pygame.Rect(posicao_oponente_x,
                                  posicao_oponente_y, 80, 180)
            tipo_de_ataque = 2  # vai servir para a animação, 2 == chute

            colisao(area_de_colisao, posicao,
                    attacking_damage, barra_de_vida_oponente)

            musica_de_soco.play()
        # ATAQUE ESPECIAL
        """if keys[pygame.K_t] and barra_de_vida_player.can_use_special() == True:

            attacking_damage = 100
            barra_de_vida_player.loose_special()
            attacked_or_not = True

            area_de_colisao = pygame.Rect(rect.x + 80, rect.y, 80, 180)

            pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
            posicao = pygame.Rect(posicao_oponente_x,
                                  posicao_oponente_y, 80, 180)
            tipo_de_ataque = 3  # vai servir para a animação, 3 == especial

            colisao(area_de_colisao, posicao,
                    attacking_damage, barra_de_vida_oponente)
"""
        if keys[pygame.K_f]:
            defendendo_ou_nao = True

    elif player == 2:  # COMANDOS DE ATAQUE PARA O PLAYER 2

        # ATAQUE DE SOCO
        if keys[pygame.K_b]:

            attacking_damage = 5 if inimigo_esta_defendendo == False else 1
            attacked_or_not = True

            area_de_colisao = pygame.Rect(
                rect.x, rect.y, -80, 100)  # área de colisão

            #pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
            posicao = pygame.Rect(posicao_oponente_x,
                                  posicao_oponente_y, 80, 180)
            tipo_de_ataque = 1  # vai servir para a animação, 1 == Soco

            colisao(area_de_colisao, posicao,
                    attacking_damage, barra_de_vida_oponente)

            musica_de_soco.play()
        # ATAQUE DE CHUTE
        if keys[pygame.K_n]:

            attacking_damage = 7 if inimigo_esta_defendendo == False else 3
            attacked_or_not = True

            area_de_colisao = pygame.Rect(rect.x - 140, rect.y + 60, 80, 150)

            #pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
            posicao = pygame.Rect(posicao_oponente_x,
                                  posicao_oponente_y, 80, 180)
            tipo_de_ataque = 2  # vai servir para a animação, 2 == chute

            colisao(area_de_colisao, posicao,
                    attacking_damage, barra_de_vida_oponente)

            musica_de_soco.play()
        # ATAQUE ESPECIAL
        """if keys[pygame.K_m] and barra_de_vida_player.can_use_special() == True:

            attacking_damage = 33
            barra_de_vida_player.loose_special()
            attacked_or_not = True

            area_de_colisao = pygame.Rect(rect.x - 80, rect.y, 80, 180)

            pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
            posicao = pygame.Rect(posicao_oponente_x,
                                  posicao_oponente_y, 80, 180)
            tipo_de_ataque = 3  # vai servir para a animação, 3 == especial

            colisao(area_de_colisao, posicao,
                    attacking_damage, barra_de_vida_oponente)"""

    return attacked_or_not, tipo_de_ataque, defendendo_ou_nao
