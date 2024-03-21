import pygame
from pygame.locals import *
from utilities.colisoes import is_colliding_left # Não está pegando sem o utilities


# define a função de movimento para ambos os personagens
def move(rect, player, ground, speed, largura, altura, inimigo, movendo_ou_nao, block):
    gravidade = 2

    colliding_right_or_left = is_colliding_left(rect, inimigo) 
    # None = não colide
    # True = colide pela esquerda
    # False = colide pela direita

    # para registrar a tecla que for pressionada
    keys = pygame.key.get_pressed()

    if player == 1 and block == False:  # determina a movimentação para o player 1 (o player que começa na esquerda)

        if keys[pygame.K_a] and (colliding_right_or_left == None or colliding_right_or_left == False):  # verifica se a tecla pressionada foi A, se for o player 1 movimenta para a esquerda e atualiza a váriavel que indica o sentido do personagem
            movendo_ou_nao = True

            rect.x -= 10

        # mesma coisa que a condição acima, mas para verificar se o personagem está andando para a direita
        if keys[pygame.K_d] and (colliding_right_or_left == None or colliding_right_or_left == True):
            movendo_ou_nao = True

            rect.x += 10
            
        # pulo do personagem: o personagem só pula se ele estiver no chão
        if keys[pygame.K_w] and ground == True:
            speed = - 20
            rect.y += speed
            ground = False

    elif player == 2 and block == False:  # mesmas condições para movimentação do personagem, mas agora para o player 2
       
        if keys[pygame.K_LEFT] and (colliding_right_or_left == None or colliding_right_or_left == False):
            movendo_ou_nao = True
            
            rect.x -= 10

        if keys[pygame.K_RIGHT] and (colliding_right_or_left == None or colliding_right_or_left == True):
            movendo_ou_nao = True

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

    if rect.bottom > altura - 135:  # o - 110 está aí porque queremos que quando ele pule ele não passe do chão e não da borda
        ground = True  # para ele poder pular de novo
        rect.bottom = altura - 135

    pressed_keys = [pygame.K_a, pygame.K_d] if player == 1 else [pygame.K_LEFT, pygame.K_RIGHT]
    is_any_movement_key_pressed = any(keys[key] for key in pressed_keys)

    # Define movendo_ou_nao com base nas condições anteriores
    movendo_ou_nao = is_any_movement_key_pressed
    
    return ground, speed, movendo_ou_nao