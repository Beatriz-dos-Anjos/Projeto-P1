import pygame
from pygame.locals import *
from utilities.functions import combate, move


class Kanye_fighter():
    def __init__(self, player, x, y):
        self.player = player
        self.rect = pygame.Rect(x, y, 80, 180)
        self.speed = 0
        self.ground = True
        self.last_attack_time = 0
        self.facing_left = True if self.player == 2 else False


    def combate(self, surface, posicao_oponente_x, posicao_oponente_y, barra_de_vida_oponente):
        attacking_countdown = 2000
        # Temporizador para o personagem só poder atacar de 2 em 2 segundos
        if pygame.time.get_ticks() - self.last_attack_time >= attacking_countdown: # confere se o tempo de execução do jogo subtraindo o tempo do último ataque realizado é maior ou igual ao countdown especulado
            self.last_attack_time = combate(self.rect, self.player, surface, self.facing_left, posicao_oponente_x, posicao_oponente_y, barra_de_vida_oponente) 
            

    def move(self, largura, altura):
        self.facing_left, self.ground, self.speed = move(self.rect, self.player, self.facing_left, self.ground, self.speed, largura, altura)


    def return_x_y(self):
        return (self.rect.x, self.rect.y)


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def get_rect(self):
        return self.rect
