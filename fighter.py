import pygame
from pygame.locals import *


class Fighter():
    def __init__(self, player, x, y):
        self.player = player
        self.rect = pygame.Rect(x, y, 80, 180)
        self.speed = 0
        self.ground = False

    def move(self, largura, altura):
        # gravidade
        gravidade = 2

        # Movimentos para esquerda e direita
        # para o movimento continuar enquanto for pressionado
        keys = pygame.key.get_pressed()
        if self.player == 1:  # determina se vai ser o jogador 1 ou 2
            if keys[pygame.K_a]:
                self.rect.x -= 10
            if keys[pygame.K_d]:
                self.rect.x += 10

            # Pulo do personagem
            # a condição é para ele só poder pular se estiver no chão
            if keys[pygame.K_w] and self.ground == False:
                self.speed = - 20
                self.rect.y += self.speed
                self.ground = True

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
                self.ground = False  # para ele poder pular de novo
                self.rect.bottom = altura - 110

        # agora o mesmo código para o jogaodor 2, mudando as letras keys
        if self.player == 2:
            if keys[pygame.K_LEFT]:
                self.rect.x -= 10
            if keys[pygame.K_RIGHT]:
                self.rect.x += 10

            # Pulo do personagem
            # a condição é para ele só poder pular se estiver no chão
            if keys[pygame.K_UP] and self.ground == False:
                self.speed = - 20
                self.rect.y += self.speed
                self.ground = True

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
                self.ground = False  # para ele poder pular de novo
                self.rect.bottom = altura - 110

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
