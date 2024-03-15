import pygame
from pygame.locals import *
from utilities.colisoes import colisao # Não está pegando sem o utilities


def combate(rect, player, surface, facing_left, posicao_oponente_x, posicao_oponente_y, barra_de_vida_oponente, barra_de_vida_player):
        attacking_damage = 0
        last_attack_time = 0
        
        keys = pygame.key.get_pressed()

        if player == 1:  # COMANDOS DE ATAQUE PARA O PLAYER 1

            # ATAQUE DE SOCO
            if keys[pygame.K_e]:

                attacking_damage = 5  # Quantidade de dano
                last_attack_time = pygame.time.get_ticks()  # registra o momento em que o personagem deu o último ataque

                # verifica se ele está virado para a esquerda ou a direita 
                if facing_left == False:
                    area_de_colisao = pygame.Rect(rect.x + 80, rect.y, 80, 180)  #área de colisão

                elif facing_left == True:
                    area_de_colisao = pygame.Rect(rect.x - 80, rect.y, 80, 180)

                pygame.draw.rect(surface, (0, 255, 0), area_de_colisao) # desenha a hitbox do ataque
                posicao = pygame.Rect(posicao_oponente_x, posicao_oponente_y, 80, 180)  # desenha a hit box do personagem inimigo 

                colisao(area_de_colisao, posicao, attacking_damage, barra_de_vida_oponente)  # invoca a função para verificar se houve colisão entre o golpe e o inimigo 
            
            # ATAQUE DE CHUTE
            if keys[pygame.K_r]:

                attacking_damage = 7  
                last_attack_time = pygame.time.get_ticks() 
                
                if facing_left == False:
                    area_de_colisao = pygame.Rect(rect.x + 80, rect.y, 80, 180)

                elif facing_left == True:
                    area_de_colisao = pygame.Rect(rect.x - 80, rect.y, 80, 180)

                pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
                posicao = pygame.Rect(posicao_oponente_x, posicao_oponente_y, 80, 180)

                colisao(area_de_colisao, posicao, attacking_damage, barra_de_vida_oponente)

            # ATAQUE ESPECIAL
            if keys[pygame.K_t] and barra_de_vida_player.can_use_special() == True:

                attacking_damage = 33
                last_attack_time = pygame.time.get_ticks() 
                barra_de_vida_player.loose_special()
                
                if facing_left == False:
                    area_de_colisao = pygame.Rect(rect.x + 80, rect.y, 80, 180)

                elif facing_left == True:
                    area_de_colisao = pygame.Rect(rect.x - 80, rect.y, 80, 180)

                pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
                posicao = pygame.Rect(posicao_oponente_x, posicao_oponente_y, 80, 180)

                colisao(area_de_colisao, posicao, attacking_damage, barra_de_vida_oponente)


        elif player == 2:  # COMANDOS DE ATAQUE PARA O PLAYER 2

            # ATAQUE DE SOCO
            if keys[pygame.K_b]:

                attacking_damage = 5
                last_attack_time = pygame.time.get_ticks()

                if facing_left == False:
                    area_de_colisao = pygame.Rect(rect.x + 80, rect.y, 80, 180)

                elif facing_left == True:
                    area_de_colisao = pygame.Rect(rect.x - 80, rect.y, 80, 180)

                pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
                posicao = pygame.Rect(posicao_oponente_x, posicao_oponente_y, 80, 180)

                colisao(area_de_colisao, posicao, attacking_damage, barra_de_vida_oponente)

            # ATAQUE DE CHUTE
            if keys[pygame.K_n]:

                attacking_damage = 7  
                last_attack_time = pygame.time.get_ticks() 
                
                if facing_left == False:
                    area_de_colisao = pygame.Rect(rect.x + 80, rect.y, 80, 180)

                elif facing_left == True:
                    area_de_colisao = pygame.Rect(rect.x - 80, rect.y, 80, 180)

                pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
                posicao = pygame.Rect(posicao_oponente_x, posicao_oponente_y, 80, 180)

                colisao(area_de_colisao, posicao, attacking_damage, barra_de_vida_oponente)

            # ATAQUE ESPECIAL
            if keys[pygame.K_m] and barra_de_vida_player.can_use_special() == True:

                attacking_damage = 33 
                last_attack_time = pygame.time.get_ticks() 
                barra_de_vida_player.loose_special()

                
                if facing_left == False:
                    area_de_colisao = pygame.Rect(rect.x + 80, rect.y, 80, 180)

                elif facing_left == True:
                    area_de_colisao = pygame.Rect(rect.x - 80, rect.y, 80, 180)

                pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
                posicao = pygame.Rect(posicao_oponente_x, posicao_oponente_y, 80, 180)

                colisao(area_de_colisao, posicao, attacking_damage, barra_de_vida_oponente)

        return last_attack_time
