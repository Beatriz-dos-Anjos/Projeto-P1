import pygame
from pygame.locals import *


class funcoes():
    def __init__(self):
        pass

    def colisao(self, hitbox, player, golpe, barra_de_vida):
        # se o retângulo equivalente a hitbox e o retângulo equivalente a hitbox do personagem, vai ativar a função de loose_health
        if hitbox.colliderect(player):
            barra_de_vida.loose_health(golpe)
    

