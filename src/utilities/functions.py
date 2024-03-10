import pygame
from pygame.locals import *

# Classe de funções criada para deixar o código mais legível e mais simples de entender
# estávamos criando várias funções iguais em todos


def colisao(hitbox, player, golpe, barra_de_vida):
    # se o retângulo equivalente a hitbox e o retângulo equivalente a hitbox do personagem, vai ativar a função de loose_health
    if hitbox.colliderect(player):
        barra_de_vida.loose_health(golpe)


# define a função de movimento para ambos os personagens
def move(rect, player, facing_left, ground, speed, largura, altura):
    gravidade = 2

    # para registrar a tecla que for pressionada
    keys = pygame.key.get_pressed()

    if player == 1:  # determina a movimentação para o player 1 (o player que começa na esquerda)

        if keys[pygame.K_a]:  # verifica se a tecla pressionada foi A, se for o player 1 movimenta para a esquerda e atualiza a váriavel que indica o sentido do personagem
            facing_left = True  
            rect.x -= 10  

        # mesma coisa que a condição acima, mas para verificar se o personagem está andando para a direita
        if keys[pygame.K_d]:
            facing_left = False
            rect.x += 10

        # pulo do personagem: o personagem só pula se ele estiver no chão
        if keys[pygame.K_w] and ground == True:
            speed = - 20
            rect.y += speed
            ground = False

    elif player == 2:  # mesmas condições para movimentação do personagem, mas agora para o player 2
       
        if keys[pygame.K_LEFT]:
            facing_left = True
            rect.x -= 10

        if keys[pygame.K_RIGHT]:
            facing_left = False
            rect.x += 10

        if keys[pygame.K_UP] and ground == True:
            speed = - 20
            rect.y += speed
            ground = False
    
    # Para ele voltar depois do pulo
    speed += gravidade
    rect.y += speed

    # Impedir que o personagem saia das bordas da tela
    if rect.left < 0:
        rect.left = 0

    if rect.right > largura:
        rect.right = largura

    if rect.top < 0:
        rect.top = 0

    if rect.bottom > altura - 110:  # o - 110 está aí porque queremos que quando ele pule ele não passe do chão e não da borda
        ground = True  # para ele poder pular de novo
        rect.bottom = altura - 110
    
    return facing_left, ground, speed


def combate(rect, player, surface, facing_left, posicao_oponente_x, posicao_oponente_y, barra_de_vida_oponente):
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
            if keys[pygame.K_t]:

                attacking_damage = 33
                last_attack_time = pygame.time.get_ticks() 
                
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
            if keys[pygame.K_m]:

                attacking_damage = 33 
                last_attack_time = pygame.time.get_ticks() 
                
                if facing_left == False:
                    area_de_colisao = pygame.Rect(rect.x + 80, rect.y, 80, 180)

                elif facing_left == True:
                    area_de_colisao = pygame.Rect(rect.x - 80, rect.y, 80, 180)

                pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
                posicao = pygame.Rect(posicao_oponente_x, posicao_oponente_y, 80, 180)

                colisao(area_de_colisao, posicao, attacking_damage, barra_de_vida_oponente)

        return last_attack_time


def gaining_health(self,qtd_ganha):  #função criada pra ganhar vida
    self.life +=qtd_ganha
