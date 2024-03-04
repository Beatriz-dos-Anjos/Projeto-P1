import pygame
from pygame.locals import *


class Taylor_fighter():
    def __init__(self, player, x, y):
        self.player = player
        self.rect = pygame.Rect(x, y, 80, 180)
        self.speed = 0
        self.ground = True
        self.attacking = False
        self.attacking_type = 0
        self.last_attack_time = 0
        self.attacking_coutdown = 2000
        self.facing_left = True if self.player == 2 else False


    def combate(self, surface):
        keys = pygame.key.get_pressed()
        if self.player == 1:
            if keys[pygame.K_e] and self.attacking == False:
                # tipo do ataque Ataque 1 = Soco
                self.attacking_type = 1
                # fala para o jogo que o personagem está atacando o golpe 1
                self.attacking = True
                # registra o momento em que o personagem deu o último ataque
                self.last_attack_time = pygame.time.get_ticks()
                # calcula a área de colisão do soco em relação a posição atual do jogador
                # verifica se ele está virado para a esquerda ou a direita 
                if self.facing_left == False:
                    area_de_colisao = pygame.Rect(self.rect.x + 80, self.rect.y, 80, 180)
                elif self.facing_left == True:
                    area_de_colisao = pygame.Rect(self.rect.x - 80, self.rect.y, 80, 180)
                # desenha a área de colisão
                pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
        elif self.player == 2:
            if keys[pygame.K_n] and self.attacking == False:
                # tipo do ataque Ataque 1 = Soco
                self.attacking_type = 1
                # fala para o jogo que o personagem está atacando o golpe 1
                self.attacking = True
                # registra o momento em que o personagem deu o último ataque
                self.last_attack_time = pygame.time.get_ticks()
                # calcula a área de colisão do soco em relação a posição atual do jogador
                if self.facing_left == False:
                    area_de_colisao = pygame.Rect(self.rect.x + 80, self.rect.y, 80, 180)
                elif self.facing_left == True:
                    area_de_colisao = pygame.Rect(self.rect.x - 80, self.rect.y, 80, 180)
                # desenha a área de colisão
                pygame.draw.rect(surface, (0, 255, 0), area_de_colisao)
            # implementar o ataque dois, que no caso é o chute 

        # Temporizador para o personagem só poder atacar de 2 em 2 segundos
        if pygame.time.get_ticks() - self.last_attack_time >= self.attacking_coutdown:
            self.attacking = False


    def move(self, largura, altura):
        # gravidade
        gravidade = 2

        # Movimentos para esquerda e direita
        # para o movimento continuar enquanto for pressionado
        keys = pygame.key.get_pressed()
        if self.player == 1:  # determina se vai ser o jogador 1 ou 2
            if keys[pygame.K_a]:
                self.facing_left = False
                self.rect.x -= 10
            if keys[pygame.K_d]:
                self.facing_left = True
                self.rect.x += 10

            # Pulo do personagem:: o personagem só pula se ele estiver no chão
            if keys[pygame.K_w] and self.ground == True:
                self.speed = - 20
                self.rect.y += self.speed
                self.ground = False

            # Para ele voltar depois do pulo
            self.speed += gravidade
            self.rect.y += self.speed

            # Impedir que o personagem saia das bordas da tela
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > largura:
                self.rect.right = largura
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > altura - 110:  # o - 110 está aí porque queremos que quando ele pule ele não passe do chão e não da borda
                self.ground = True  # para ele poder pular de novo
                self.rect.bottom = altura - 110


        elif self.player == 2:  # determina se vai ser o jogador 1 ou 2
            if keys[pygame.K_LEFT]:
                self.facing_left = False
                self.rect.x -= 10
            if keys[pygame.K_RIGHT]:
                self.facing_left = True
                self.rect.x += 10

            # Pulo do personagem:: o personagem só pula se ele estiver no chão
            if keys[pygame.K_UP] and self.ground == True:
                self.speed = - 20
                self.rect.y += self.speed
                self.ground = False

            # Para ele voltar depois do pulo
            self.speed += gravidade
            self.rect.y += self.speed

            # Impedir que o personagem saia das bordas da tela
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > largura:
                self.rect.right = largura
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > altura - 110:  # o - 110 está aí porque queremos que quando ele pule ele não passe do chão e não da borda
                self.ground = True  # para ele poder pular de novo
                self.rect.bottom = altura - 110


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
